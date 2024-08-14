from django import forms

class TextSizeForm(forms.Form):
    RADIO_CHOICES = [
        ('small', 'Small'),
        ('default', 'Default'),
        ('larger', 'Larger'),
    ]

    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.RadioSelect(),
    )

class ColorAndContrast(forms.Form):
    RADIO_CHOICES = [
        ('high_contrast', 'High Contrast (Classic)'),
        ('design_tweaks', 'Design Tweaks (Modern)'),
        ('reverse', 'Reverse'),
    ]

    selected_option = forms.ChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.RadioSelect(),
    )

class Linespacing(forms.Form):
    LINE_SPACING_CHOICES = [
        ('one_two', 'One Two'),
        ('one_two_three', 'One Two Three'),
        ('reverse', 'One Two Three'),
    ]

    selected_option = forms.ChoiceField(
        choices=LINE_SPACING_CHOICES,
        widget=forms.RadioSelect(),
    )

class PageWidth(forms.Form):
    PAGE_WIDTH_CHOICES = [
        ('fixed_width', 'Fixed width: for easier reading, all content in a column'),
        ('full_width', 'Full width: for easier skimming and wide tables or galleries'),
    ]

    selected_option = forms.ChoiceField(
        choices=PAGE_WIDTH_CHOICES,
        widget=forms.RadioSelect(),
    )
