from edc_constants.constants import ALIVE
from edc_form_validators import FormValidator


class HomeVisitFormValidator(FormValidator):

    def clean(self):

        self.not_required_if(
            'research_team',
            field='clinician_type',
            field_required='clinician_facility')

        self.required_if(
            ALIVE,
            field='visit_outcome',
            field_required='next_appointment',)

        self.required_if(
            ALIVE,
            field='visit_outcome',
            field_required='next_ap_type',)

        other_fields = ['clinician_type', 'clinician_facility',
                        'visit_outcome', 'next_ap_facility', ]

        for other_field in other_fields:
            self.validate_other_specify(
                field=other_field,)