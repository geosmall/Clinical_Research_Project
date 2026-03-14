"""
Generate a representative synthetic clinical trial starter dataset for this repo's
8-week learning plan and capstone project.

Outputs:
- Writes CSV files plus README/data dictionary documentation to `./data` by default
- Use `--outdir` to write to a different folder

Command-line usage:
- `python Dad_Stuff\\synthetic_trial_data\\make_synthetic_trial_data.py`
- `python Dad_Stuff\\synthetic_trial_data\\make_synthetic_trial_data.py --seed 42`
- `python Dad_Stuff\\synthetic_trial_data\\make_synthetic_trial_data.py --outdir data`
"""

import argparse
import csv
import os
import random
import subprocess
from datetime import date, timedelta


VISIT_SCHEDULE = [
    ("Screening", -7),
    ("Baseline", 0),
    ("Week 4", 28),
    ("Week 8", 56),
    ("Week 12", 84),
]

SITE_BLUEPRINTS = [
    ("S001", "Buffalo Clinical Research Center", "Buffalo", "NY", "Northeast", 24, 0.86),
    ("S002", "Rochester Trial Institute", "Rochester", "NY", "Northeast", 20, 0.80),
    ("S003", "Cleveland Study Network", "Cleveland", "OH", "Midwest", 22, 0.76),
    ("S004", "Pittsburgh Medical Research Group", "Pittsburgh", "PA", "Northeast", 18, 0.72),
    ("S005", "Columbus Clinical Trials Unit", "Columbus", "OH", "Midwest", 26, 0.68),
    ("S006", "Albany Research Associates", "Albany", "NY", "Northeast", 16, 0.62),
]

RACES = ["White", "Black or African American", "Asian", "Other", "Unknown"]
SEXES = ["F", "M"]
ARMS = ["Treatment", "Control"]
AE_TERMS = [
    "Headache",
    "Nausea",
    "Fatigue",
    "Dizziness",
    "Injection site reaction",
    "Upper respiratory infection",
    "Insomnia",
    "Diarrhea",
]
DEVIATION_NOTES = {
    "Missed visit window": "Visit occurred outside the allowed protocol window.",
    "Late lab collection": "Protocol-required lab sample collected late.",
    "Missed assessment": "Required study assessment not completed at visit.",
    "Informed consent issue": "Consent documentation required clarification or correction.",
    "Dosing deviation": "Investigational product administration differed from plan.",
}
SCREEN_FAIL_REASONS = [
    "Inclusion criteria not met",
    "Abnormal screening laboratory value",
    "Withdrew consent before randomization",
    "Investigator decision",
]
DISCONTINUATION_REASONS = [
    "Adverse event",
    "Lost to follow-up",
    "Withdrawal by subject",
    "Protocol deviation",
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a representative synthetic clinical trial starter dataset."
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducible output.")
    parser.add_argument(
        "--outdir",
        default="data",
        help="Output directory for generated CSV and Markdown files.",
    )
    return parser.parse_args()


def iso(value):
    return "" if value is None else str(value)


def write_csv(outdir, filename, rows):
    if not rows:
        return
    with open(os.path.join(outdir, filename), "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def get_git_commit_info():
    try:
        full_hash = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        short_hash = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        return short_hash, full_hash
    except (OSError, subprocess.CalledProcessError):
        return "unknown", "unknown"


def make_sites(rng, study_start):
    sites = []
    for index, (site_id, name, city, state, region, enrollment_target, performance_score) in enumerate(
        SITE_BLUEPRINTS, start=1
    ):
        activation_date = study_start + timedelta(days=(index - 1) * 10 + rng.randint(0, 5))
        site_status = "Monitoring" if performance_score < 0.66 else "Active"
        sites.append(
            {
                "site_id": site_id,
                "site_name": name,
                "city": city,
                "state": state,
                "region": region,
                "site_activation_date": iso(activation_date),
                "site_status": site_status,
                "principal_investigator": f"PI {city.split()[0]}",
                "enrollment_target": enrollment_target,
                "screen_failure_rate_target": round(1.0 - performance_score + 0.10, 2),
                "monitoring_risk_level": "High" if performance_score < 0.66 else "Standard",
            }
        )
    return sites


def build_subject_record(subject_id, site_id, screening_number, screening_date, sex, age, race):
    return {
        "subject_id": subject_id,
        "site_id": site_id,
        "screening_number": screening_number,
        "screening_date": iso(screening_date),
        "screen_fail_flag": "N",
        "screen_fail_reason": "",
        "randomization_number": "",
        "sex": sex,
        "age": age,
        "race": race,
        "treatment_arm": "",
        "enrollment_date": "",
        "baseline_date": "",
        "subject_status": "Screened",
        "completion_date": "",
        "discontinuation_date": "",
        "discontinuation_reason": "",
    }


def append_visit(visits, visit_id, subject_id, site_id, visit_type, planned_date, actual_date, visit_status):
    window_ok = ""
    if actual_date is not None:
        allowed_window = 3 if visit_type in {"Screening", "Baseline"} else 5
        window_ok = "Y" if abs((actual_date - planned_date).days) <= allowed_window else "N"

    visits.append(
        {
            "visit_id": visit_id,
            "subject_id": subject_id,
            "site_id": site_id,
            "visit_type": visit_type,
            "planned_date": iso(planned_date),
            "actual_date": iso(actual_date),
            "visit_status": visit_status,
            "days_from_baseline": dict(VISIT_SCHEDULE)[visit_type],
            "protocol_window_ok": window_ok,
        }
    )


def derive_visit_outcome(rng, visit_type, treatment_arm, discontinued, site_status):
    if visit_type == "Screening":
        return "Completed"
    if visit_type == "Baseline":
        return "Completed"
    if discontinued and visit_type in {"Week 8", "Week 12"} and rng.random() < 0.75:
        return "Not Done"

    weights = {
        "Completed": 0.73,
        "Rescheduled": 0.13,
        "Missed": 0.10,
        "Completed Out of Window": 0.04,
    }
    if treatment_arm == "Treatment":
        weights["Rescheduled"] += 0.02
    if site_status == "Monitoring":
        weights["Missed"] += 0.04
        weights["Completed"] -= 0.04
    pick = rng.random()
    cumulative = 0.0
    for label, weight in weights.items():
        cumulative += weight
        if pick <= cumulative:
            return label
    return "Completed"


def make_adverse_events(rng, subject, site_status, enrollment_date, last_study_day, discontinued_flag):
    events = []
    base_event_count = rng.choices([0, 1, 2, 3], weights=[0.34, 0.38, 0.20, 0.08])[0]
    if subject["treatment_arm"] == "Treatment" and rng.random() < 0.20:
        base_event_count += 1
    if discontinued_flag and rng.random() < 0.55:
        base_event_count += 1

    for _ in range(base_event_count):
        start_date = enrollment_date + timedelta(days=rng.randint(0, max(1, (last_study_day - enrollment_date).days)))
        severity = rng.choices(["Mild", "Moderate", "Severe"], weights=[0.52, 0.34, 0.14])[0]
        serious_flag = "Y" if severity == "Severe" and rng.random() < 0.55 else "N"
        if severe := (severity == "Severe" and rng.random() < 0.35):
            serious_flag = "Y"
        relatedness = rng.choices(
            ["Related", "Possibly Related", "Unrelated"],
            weights=[0.38, 0.36, 0.26] if subject["treatment_arm"] == "Treatment" else [0.20, 0.28, 0.52],
        )[0]
        action_taken = "Drug interrupted" if serious_flag == "Y" or severe else rng.choice(
            ["None", "Concomitant medication", "Dose unchanged"]
        )
        events.append(
            {
                "ae_id": "",
                "subject_id": subject["subject_id"],
                "site_id": subject["site_id"],
                "ae_term": rng.choice(AE_TERMS),
                "start_date": iso(start_date),
                "end_date": iso(start_date + timedelta(days=rng.randint(1, 12))),
                "severity": severity,
                "serious_flag": serious_flag,
                "relatedness": relatedness,
                "action_taken": action_taken,
                "outcome": rng.choice(["Recovered", "Recovering", "Not Recovered"]),
                "study_day_onset": (start_date - enrollment_date).days,
            }
        )
    if site_status == "Monitoring" and rng.random() < 0.08:
        events.append(
            {
                "ae_id": "",
                "subject_id": subject["subject_id"],
                "site_id": subject["site_id"],
                "ae_term": "Headache",
                "start_date": "",
                "end_date": "",
                "severity": "Moderate",
                "serious_flag": "N",
                "relatedness": "Possibly Related",
                "action_taken": "None",
                "outcome": "Recovering",
                "study_day_onset": "",
            }
        )
    return events


def make_protocol_deviation(rng, deviation_id, subject_id, site_id, deviation_date, deviation_type, severity):
    return {
        "deviation_id": deviation_id,
        "subject_id": subject_id,
        "site_id": site_id,
        "deviation_date": iso(deviation_date),
        "deviation_type": deviation_type,
        "severity": severity,
        "resolved_flag": rng.choice(["Y", "N"]),
        "notes": DEVIATION_NOTES[deviation_type],
    }


def build_dataset(seed):
    rng = random.Random(seed)
    study_start = date(2025, 1, 6)
    sites = make_sites(rng, study_start)
    site_lookup = {site["site_id"]: site for site in sites}

    subjects = []
    visits = []
    adverse_events = []
    protocol_deviations = []

    subject_num = 1
    visit_num = 1
    ae_num = 1
    deviation_num = 1

    for site in sites:
        performance_score = 1.0 - site["screen_failure_rate_target"]
        screened_count = max(site["enrollment_target"] + rng.randint(3, 8), 18)

        for _ in range(screened_count):
            subject_id = f"SUBJ{subject_num:03d}"
            screening_number = f"SCR{subject_num:03d}"
            screening_date = date.fromisoformat(site["site_activation_date"]) + timedelta(days=rng.randint(1, 110))
            sex = rng.choice(SEXES)
            age = rng.randint(22, 78)
            race = rng.choice(RACES)
            subject = build_subject_record(subject_id, site["site_id"], screening_number, screening_date, sex, age, race)

            screen_fail_probability = min(max(1.0 - performance_score, 0.12), 0.32)
            if rng.random() < screen_fail_probability:
                subject["screen_fail_flag"] = "Y"
                subject["screen_fail_reason"] = rng.choice(SCREEN_FAIL_REASONS)
                subject["subject_status"] = "Screen Failed"
                subjects.append(subject)

                append_visit(
                    visits,
                    f"VIS{visit_num:04d}",
                    subject_id,
                    site["site_id"],
                    "Screening",
                    screening_date,
                    screening_date + timedelta(days=rng.randint(0, 2)),
                    "Completed",
                )
                visit_num += 1
                if subject["screen_fail_reason"] == "Withdrew consent before randomization":
                    protocol_deviations.append(
                        make_protocol_deviation(
                            rng,
                            f"DEV{deviation_num:04d}",
                            subject_id,
                            site["site_id"],
                            screening_date,
                            "Informed consent issue",
                            "Major",
                        )
                    )
                    deviation_num += 1
                subject_num += 1
                continue

            enrollment_date = screening_date + timedelta(days=rng.randint(2, 10))
            treatment_arm = ARMS[(subject_num + rng.randint(0, 1)) % 2]
            subject["randomization_number"] = f"RAND{subject_num:03d}"
            subject["treatment_arm"] = treatment_arm
            subject["enrollment_date"] = iso(enrollment_date)
            subject["baseline_date"] = iso(enrollment_date)

            discontinued = rng.random() < (0.16 if treatment_arm == "Control" else 0.20)
            completion_date = enrollment_date + timedelta(days=84)
            discontinuation_date = None
            discontinuation_reason = ""
            if discontinued:
                discontinuation_date = enrollment_date + timedelta(days=rng.choice([28, 42, 56, 70]))
                discontinuation_reason = rng.choice(DISCONTINUATION_REASONS)

            if discontinued:
                subject["subject_status"] = "Discontinued"
                subject["discontinuation_date"] = iso(discontinuation_date)
                subject["discontinuation_reason"] = discontinuation_reason
            else:
                subject["subject_status"] = "Completed" if completion_date <= date(2025, 7, 31) else "Active"
                if subject["subject_status"] == "Completed":
                    subject["completion_date"] = iso(completion_date)

            subjects.append(subject)

            last_study_day = discontinuation_date or completion_date
            for visit_type, offset in VISIT_SCHEDULE:
                if visit_type != "Screening":
                    planned_date = enrollment_date + timedelta(days=offset)
                else:
                    planned_date = screening_date

                if visit_type not in {"Screening", "Baseline"} and last_study_day < planned_date:
                    continue

                visit_status = derive_visit_outcome(
                    rng,
                    visit_type,
                    treatment_arm,
                    discontinued,
                    site["site_status"],
                )
                if visit_status == "Completed":
                    actual_date = planned_date + timedelta(days=rng.randint(-2, 3))
                elif visit_status == "Completed Out of Window":
                    actual_date = planned_date + timedelta(days=rng.choice([-9, -7, 7, 10]))
                elif visit_status == "Rescheduled":
                    actual_date = planned_date + timedelta(days=rng.randint(4, 9))
                else:
                    actual_date = None

                append_visit(
                    visits,
                    f"VIS{visit_num:04d}",
                    subject_id,
                    site["site_id"],
                    visit_type,
                    planned_date,
                    actual_date,
                    visit_status,
                )
                visit_num += 1

                if visit_status == "Completed Out of Window":
                    protocol_deviations.append(
                        make_protocol_deviation(
                            rng,
                            f"DEV{deviation_num:04d}",
                            subject_id,
                            site["site_id"],
                            actual_date,
                            "Missed visit window",
                            "Minor",
                        )
                    )
                    deviation_num += 1
                elif visit_status == "Missed":
                    protocol_deviations.append(
                        make_protocol_deviation(
                            rng,
                            f"DEV{deviation_num:04d}",
                            subject_id,
                            site["site_id"],
                            planned_date,
                            "Missed assessment",
                            "Major" if visit_type in {"Baseline", "Week 12"} else "Minor",
                        )
                    )
                    deviation_num += 1
                elif visit_status == "Rescheduled" and rng.random() < 0.55:
                    protocol_deviations.append(
                        make_protocol_deviation(
                            rng,
                            f"DEV{deviation_num:04d}",
                            subject_id,
                            site["site_id"],
                            actual_date,
                            "Late lab collection",
                            "Minor",
                        )
                    )
                    deviation_num += 1

            if discontinued and discontinuation_reason == "Protocol deviation":
                protocol_deviations.append(
                    make_protocol_deviation(
                        rng,
                        f"DEV{deviation_num:04d}",
                        subject_id,
                        site["site_id"],
                        discontinuation_date,
                        "Dosing deviation",
                        "Major",
                    )
                )
                deviation_num += 1

            subject_aes = make_adverse_events(
                rng,
                subject,
                site["site_status"],
                enrollment_date,
                last_study_day,
                discontinued,
            )
            for event in subject_aes:
                event["ae_id"] = f"AE{ae_num:04d}"
                ae_num += 1
                adverse_events.append(event)

            subject_num += 1

    return sites, subjects, visits, adverse_events, protocol_deviations


def write_readme(outdir, seed, tables):
    sites, subjects, visits, adverse_events, protocol_deviations = tables
    screen_fail_count = sum(1 for row in subjects if row["screen_fail_flag"] == "Y")
    randomized_count = sum(1 for row in subjects if row["randomization_number"])
    completed_count = sum(1 for row in subjects if row["subject_status"] == "Completed")
    discontinued_count = sum(1 for row in subjects if row["subject_status"] == "Discontinued")
    output_path = os.path.abspath(outdir)
    script_path = os.path.abspath(__file__)
    short_commit, full_commit = get_git_commit_info()

    with open(os.path.join(outdir, "README_data.md"), "w", encoding="utf-8") as handle:
        handle.write(
            "# Synthetic Clinical Trial Dataset\n\n"
            "Representative starter dataset for the Clinical Research Learning Final Pack.\n\n"
            "## Generation Notes\n"
            f"- Seed: {seed}\n"
            "- Data type: fully synthetic, privacy-safe, non-patient data\n"
            "- Scenario: multi-site interventional study with screening, enrollment, scheduled visits, adverse events, and protocol deviations\n\n"
            "## Source and Provenance\n"
            f"- Output folder: `{output_path}`\n"
            f"- Generated by: `{script_path}`\n"
            f"- Git commit: `{short_commit}` (`{full_commit}`)\n\n"
            "## Table Counts\n"
            f"- sites.csv: {len(sites)} rows\n"
            f"- subjects.csv: {len(subjects)} rows\n"
            f"- visits.csv: {len(visits)} rows\n"
            f"- adverse_events.csv: {len(adverse_events)} rows\n"
            f"- protocol_deviations.csv: {len(protocol_deviations)} rows\n\n"
            "## Subject Disposition Summary\n"
            f"- Randomized subjects: {randomized_count}\n"
            f"- Screen failures: {screen_fail_count}\n"
            f"- Completed subjects: {completed_count}\n"
            f"- Discontinued subjects: {discontinued_count}\n\n"
            "## Suggested Use\n"
            "- SQL practice for enrollment, screen failure rates, visit completion, site performance, safety counts, and protocol deviation trends\n"
            "- Tableau dashboards for study status, safety, and site monitoring views\n"
            "- Python exercises for data quality checks, reconciliation, and repeatable reporting\n"
        )


def write_data_dictionary(outdir):
    with open(os.path.join(outdir, "data_dictionary.md"), "w", encoding="utf-8") as handle:
        handle.write(
            "# Data Dictionary\n\n"
            "## sites.csv\n"
            "- `site_id`: unique site identifier\n"
            "- `site_activation_date`: first date the site can screen subjects\n"
            "- `screen_failure_rate_target`: planning-level site performance indicator\n"
            "- `monitoring_risk_level`: simple training label for monitoring attention\n\n"
            "## subjects.csv\n"
            "- `screen_fail_flag`: `Y` for subjects who never randomized\n"
            "- `randomization_number`: populated only for randomized subjects\n"
            "- `subject_status`: `Screen Failed`, `Active`, `Completed`, or `Discontinued`\n"
            "- `discontinuation_reason`: populated only when a subject leaves the study early\n\n"
            "## visits.csv\n"
            "- `planned_date`: protocol target date for the visit\n"
            "- `actual_date`: blank when the visit did not occur\n"
            "- `visit_status`: `Completed`, `Rescheduled`, `Missed`, `Completed Out of Window`, or `Not Done`\n"
            "- `protocol_window_ok`: blank when no actual visit occurred\n\n"
            "## adverse_events.csv\n"
            "- `serious_flag`: simple seriousness indicator used for practice analyses\n"
            "- `study_day_onset`: days from enrollment to AE onset\n"
            "- `action_taken`: simplified action relative to investigational product\n\n"
            "## protocol_deviations.csv\n"
            "- Derived mainly from visit execution or discontinuation behavior\n"
            "- `severity`: simplified `Minor` or `Major` training label\n"
        )


def main():
    args = parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    tables = build_dataset(args.seed)
    write_csv(args.outdir, "sites.csv", tables[0])
    write_csv(args.outdir, "subjects.csv", tables[1])
    write_csv(args.outdir, "visits.csv", tables[2])
    write_csv(args.outdir, "adverse_events.csv", tables[3])
    write_csv(args.outdir, "protocol_deviations.csv", tables[4])
    write_readme(args.outdir, args.seed, tables)
    write_data_dictionary(args.outdir)

    print(f"Done. Files written to ./{args.outdir}")


if __name__ == "__main__":
    main()
