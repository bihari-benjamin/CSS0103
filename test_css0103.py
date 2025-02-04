import re
import pytest

def javit_html_fajl(html_fajl_nev):
    """
    Automatikusan kijavítja a HTML fájlt a megadott feladatleírás alapján.

    Args:
        html_fajl_nev (str): A HTML fájl neve.
    """

    with open(html_fajl_nev, 'r', encoding='utf-8') as f:
        html_tartalom = f.read()

    # 1. "Boncompagni-kastély" szöveg beállítása egyes szintű fejezetcímnek
    html_tartalom = html_tartalom.replace("Boncompagni-kastély", "<h1>Boncompagni-kastély</h1>")

    # 2. Bekezdések beállítása
    html_tartalom = re.sub(r'(1855-56.*körül\.)', r'<p class="paragraph1">\1</p>', html_tartalom, flags=re.DOTALL)
    html_tartalom = re.sub(r'(Tulajdonosa.*eredeti\.)', r'<p class="paragraph2">\1</p>', html_tartalom, flags=re.DOTALL)

    # 3. Szövegformázás és stílusok
    html_tartalom = html_tartalom.replace("Hosszúsága 50 méter", "<span class='underline'>Hosszúsága 50 méter</span>")
    html_tartalom = html_tartalom.replace("gőzfűtéssel", "<span style='font-size: 22px;'>gőzfűtéssel</span>")
    html_tartalom = html_tartalom.replace("Boncompagni-Ludovisi", "<strong>Boncompagni-Ludovisi</strong>")

    # 4. CSS stílusok hozzáadása
    css_stilusok = """
    <style>
        body {
            font-family: sans-serif;
        }
        h1 {
            color: #333;
            background-color: bisque;
        }
        .paragraph1 {
            background-color: aqua;
        }
        .underline {
            text-decoration: underline;
        }
        .paragraph2 {
            background-color: antiquewhite;
        }
    </style>
    """
    html_tartalom = html_tartalom.replace("</head>", css_stilusok + "</head>")

    with open(html_fajl_nev, 'w', encoding='utf-8') as f:
        f.write(html_tartalom)

# Pytest tesztek

def test_html_exists():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content, "Az index.html fájl üres!"

def test_css_exists():
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content, "A style.css fájl üres!"

def test_html_structure():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<h1>Boncompagni-kastély</h1>' in content, "A h1 elem nem található a HTML-ben!"
        assert '<p class="paragraph1">' in content, "Az első bekezdés nem található a HTML-ben!"
        assert '<p class="paragraph2">' in content, "Az második bekezdés nem található a HTML-ben!"
        assert "<span class='underline'>Hosszúsága 50 méter</span>" in content, "Az aláhúzott szöveg nem található a HTML-ben!"
        assert '<span style=\'font-size: 22px;\'>gőzfűtéssel</span>' in content, "A 22px méretű szöveg nem található a HTML-ben!"
        assert '<strong>Boncompagni-Ludovisi</strong>' in content, "A félkövér szöveg nem található a HTML-ben!"

def test_css_structure():
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'body {' in content and 'font-family: sans-serif;' in content, "A body stílus nem található a CSS fájlban vagy nem tartalmazza a font-family-t!"
        assert 'h1 {' in content and 'color: #333;' in content and 'background-color: bisque;' in content, "A h1 stílus nem található a CSS fájlban vagy nem tartalmazza a szín és háttérszín beállításokat!"
        assert '.paragraph1 {' in content and 'background-color: aqua;' in content, "Az első bekezdés stílus nem található a CSS fájlban vagy nem tartalmazza a háttérszín beállítást!"
        assert '.paragraph2 {' in content and 'background-color: antiquewhite;' in content, "A második bekezdés stílus nem található a CSS fájlban vagy nem tartalmazza a háttérszín beállítást!"
        assert '.underline {' in content and 'text-decoration: underline;' in content, "Az aláhúzás stílus nem található a CSS fájlban!"

# Futtatás
if __name__ == '__main__':
    javit_html_fajl("index.html")
    pytest.main()