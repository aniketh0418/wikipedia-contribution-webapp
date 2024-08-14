from django.shortcuts import render
from .forms import TextSizeForm, ColorAndContrast, Linespacing, PageWidth

def homepage(request):
    if request.method == 'POST':
        form1 = TextSizeForm(request.POST)
        form2 = ColorAndContrast(request.POST)
        form3 = Linespacing(request.POST)
        form4 = PageWidth(request.POST)
        
        if form1.is_valid():
            text_size = form1.cleaned_data.get('selected_option', 'default')
            print("Form 1 submitted with text_size:", text_size)
        else:
            text_size = 'default'
        
        if form2.is_valid():
            color_and_contrast = form2.cleaned_data.get('selected_option', 'high_contrast')
        else:
            color_and_contrast = 'high_contrast'
        
        if form3.is_valid():
            line_spacing = form3.cleaned_data.get('selected_option', 'one_two_three')
        else:
            line_spacing = 'one_two_three'
        
        if form4.is_valid():
            page_width = form4.cleaned_data.get('selected_option', 'full_width')
        else:
            page_width = 'full_width'

    else:
        form1 = TextSizeForm()
        form2 = ColorAndContrast()
        form3 = Linespacing()
        form4 = PageWidth()

        text_size = 'default'
        color_and_contrast = 'high_contrast'
        line_spacing = 'one_two_three'
        page_width = 'full_width'
    
    forms = {
        'form1': form1, 
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'text_size': text_size,
        'color_and_contrast': color_and_contrast,
        'line_spacing': line_spacing,
        'page_width': page_width,
    }

    return render(request, 'home/index1.html', forms)
