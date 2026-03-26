
import os

# Configuration for all pages to be generated
pages = [
    {
        "filename": "neubau.html",
        "title": "Neubau",
        "headline": "Neubau",
        "image": "Pictures/Neubau_Dachstuhl.webp",
        "desc": "Ihr Neubau-Projekt mit der Zimmerei Müller. Wir realisieren Ihren Traum vom Eigenheim."
    },
    {
        "filename": "dachsanierung.html",
        "title": "Dachsanierung",
        "headline": "Dachsanierung",
        "image": "Pictures/Dachsanierung.webp",
        "desc": "Professionelle Dachsanierung für Werterhalt und Energieeffizienz."
    },
    {
        "filename": "holzrahmenbau.html",
        "title": "Holzrahmenbau",
        "headline": "Holzrahmenbau",
        "image": "Pictures/Holzrahmenbau.webp",
        "desc": "Moderner Holzrahmenbau: Flexibel, ökologisch und schnell."
    },
    {
        "filename": "dachfenster.html",
        "title": "Dachfenster",
        "headline": "Dachfenster",
        "image": "Pictures/Dachfenster.webp",
        "desc": "Mehr Licht und Luft mit neuen Dachfenstern. Einbau und Austausch vom Profi."
    },
    {
        "filename": "aufstockungen.html",
        "title": "Aufstockungen",
        "headline": "Aufstockungen",
        "image": "Pictures/Aufstockung-neu-modifiziert.webp",
        "desc": "Mehr Wohnraum durch Aufstockung. Wir erweitern Ihr Gebäude nach oben."
    },
    {
        "filename": "asbestsanierung.html",
        "title": "Asbestsanierung",
        "headline": "Asbestsanierung",
        "image": "Pictures/Asbestsanierung.webp",
        "desc": "Fachgerechte Asbestsanierung nach TRGS 519. Sicherheit geht vor."
    },
    {
        "filename": "treppenbau.html",
        "title": "Treppenbau",
        "headline": "Treppenbau",
        "image": "Pictures/Treppe.webp",
        "desc": "Individuelle Holztreppen – Funktionalität und Design in Perfektion."
    },
    {
        "filename": "dachgauben.html",
        "title": "Dachgauben",
        "headline": "Dachgauben",
        "image": "Pictures/Dachgaube.webp",
        "desc": "Dachgauben für mehr Platz und Licht im Dachgeschoss."
    }
]

# Read the template
with open('massivholzhaus.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Placeholder content for the accordions
placeholder_philosophy = """
<p>Hier steht bald ausführlicher Text zum Thema {title}. Wir arbeiten derzeit noch an den detaillierten Inhalten für diese Seite.</p>
<p>Unsere Philosophie bei {title} ist es, höchste Qualität mit handwerklicher Präzision zu verbinden. Jedes Projekt wird individuell geplant und auf Ihre Bedürfnisse zugeschnitten.</p>
"""

placeholder_services = """
<p>Unsere Leistungen im Bereich {title} umfassen:</p>
<ul>
    <li>Individuelle Beratung vor Ort</li>
    <li>Detaillierte Planung und Konstruktion</li>
    <li>Fachgerechte Ausführung durch unser Team</li>
    <li>Verwendung hochwertiger Materialien</li>
    <li>Langjährige Erfahrung und Kompetenz</li>
</ul>
"""

# Generate each page
for page in pages:
    new_content = template_content
    
    # Replace basic meta
    new_content = new_content.replace('Massivholzhaus | Zimmerei Müller', f'{page["title"]} | Zimmerei Müller')
    new_content = new_content.replace('Massivholzhaus – Gesundes Wohnen und ökologische Verantwortung. Erfahren Sie mehr über unsere Philosophie und Leistungen.', page["desc"])
    
    # Replace header/visuals
    new_content = new_content.replace('<h1 class="detail-title">Massivholzhaus</h1>', f'<h1 class="detail-title">{page["headline"]}</h1>')
    new_content = new_content.replace('Pictures/Bsp-SORA1.webp', page["image"])
    new_content = new_content.replace('alt="Massivholzhaus Zimmerei Müller"', f'alt="{page["headline"]} Zimmerei Müller"')
    
    # Replace Accordion Titles
    new_content = new_content.replace('Warum Massivholzhaus? Unsere Philosophie', f'Warum {page["title"]}? Unsere Philosophie')
    new_content = new_content.replace('Ihr Projekt in guten Händen: Unsere Leistungen', f'Ihr Projekt in guten Händen: Unsere Leistungen')
    
    # Replace Accordion Content (Philosophie)
    # We find the content block for philosophy and replace it. 
    # Since doing exact regex replacement on HTML block can be tricky if formatting changes, 
    # we'll look for the container div or reconstruct the accordion body content.
    
    # Strategy: Reconstruction is cleaner. We know the structure of massivholzhaus.html.
    # We will simply locate the "Philosophy" accordion body content.
    
    # Let's try a simpler approach since we know the exact string from the file we just wrote.
    # We'll identify the start and end of the first accordion content.
    
    start_marker_phi = '<div class="accordion-content">'
    end_marker_phi = '</div>'
    
    # Because there are two "accordion-content" divs, we need to be careful.
    # The first one is Philosophy, the second is Services.
    
    parts = new_content.split('<div class="accordion-content">')
    # parts[0] is everything before first accordion content
    # parts[1] is first accordion content + rest
    # parts[2] is second accordion content + rest
    
    # Process part 1 (Philosophy)
    subparts_phi = parts[1].split('</div>', 1)
    old_phi_content = subparts_phi[0]
    rest_phi = subparts_phi[1]
    
    # Process part 2 (Services)
    subparts_serv = parts[2].split('</div>', 1)
    old_serv_content = subparts_serv[0]
    rest_serv = subparts_serv[1]
    
    # Insert new content
    new_phi_content = placeholder_philosophy.format(title=page["title"])
    new_serv_content = placeholder_services.format(title=page["title"])
    
    # Reassemble
    final_content = (
        parts[0] + 
        '<div class="accordion-content">' + new_phi_content + '</div>' + 
        rest_phi + # This technically contains the part between the two accordions up to the second <div class="accordion-content"> split point? 
                   # Wait, split removes the delimiter.
                   # Let's re-verify the split logic.
                   # content = part0 + delimiter + part1 + delimiter + part2
        # However, part1 included the "middle" HTML between the end of div 1 and start of div 2.
        # Actually split is:
        # [0]: ... <button ...
        # [1]: text... </div> ... <button...
        # [2]: text... </div> ... 
        
        # So:
        # Reconstruct:
        # part[0] + delim + new_phi + </div> + (everything in part[1] AFTER the first </div>) + delim + new_serv + </div> + (everything in part[2] AFTER the first </div>)
        
        # Wait, part[1] content is: " <p>Text...</p> ... </div> ... "
        # We split part[1] by </div>. subparts_phi[0] is the text. subparts_phi[1] is the HTML between the accordions.
        
        # Correct Reassembly:
        parts[0] + 
        '<div class="accordion-content">' + 
        new_phi_content + 
        '</div>' + 
        subparts_phi[1] + 
        '<div class="accordion-content">' + 
        new_serv_content + 
        '</div>' + 
        subparts_serv[1]
    )
    
    with open(page["filename"], 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Generated {page['filename']}")
