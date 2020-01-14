class FormControlsStylerMixin:
    fields = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # forwards all unused arguments
        if self.fields:
            self.set_control_attrs()

    def set_control_attrs(self):
        for field in self.fields:
            if field in ['avatar', 'image']:
                self.fields[field].widget.attrs.update({'class': 'custom-file-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    @staticmethod
    def set_validation_attrs(form):
        for field in form.fields:
            styles = form[field].field.widget.attrs.get('class', )
            if form[field].errors:
                styles += ' is-invalid'
            else:
                styles += ' is-valid'
            form[field].field.widget.attrs.update({'class': styles})
        return form

