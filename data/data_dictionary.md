# Data Dictionary

## sites.csv
- `site_id`: unique site identifier
- `site_activation_date`: first date the site can screen subjects
- `screen_failure_rate_target`: planning-level site performance indicator
- `monitoring_risk_level`: simple training label for monitoring attention

## subjects.csv
- `screen_fail_flag`: `Y` for subjects who never randomized
- `randomization_number`: populated only for randomized subjects
- `subject_status`: `Screen Failed`, `Active`, `Completed`, or `Discontinued`
- `discontinuation_reason`: populated only when a subject leaves the study early

## visits.csv
- `planned_date`: protocol target date for the visit
- `actual_date`: blank when the visit did not occur
- `visit_status`: `Completed`, `Rescheduled`, `Missed`, `Completed Out of Window`, or `Not Done`
- `protocol_window_ok`: blank when no actual visit occurred

## adverse_events.csv
- `serious_flag`: simple seriousness indicator used for practice analyses
- `study_day_onset`: days from enrollment to AE onset
- `action_taken`: simplified action relative to investigational product

## protocol_deviations.csv
- Derived mainly from visit execution or discontinuation behavior
- `severity`: simplified `Minor` or `Major` training label
