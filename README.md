Główny branch to okrojony szablon aplikacji  

main.py - uruchomienie, routing
templates - szablony jinja2 
- scaffold.html.j2 - szablon bazowy
- /pages - strony docelowe wskazywane w routingu
- /errors - strony błędów serwera (404, 500...)

##################
Odpalenie venv 
source .venv/bin/activate
"projekt"\Scripts\activate [win] 

Aktualizacja req
pip3 freeze > requirements.txt

robimy dockera
docker image build -t modular_costam

.gitignore
Każdy robi sobie sam. Ja mam pracuję na 2 systemach i kazdy mam inny więc poleciłem sobie "git ignore .gitignore"  

requirements.txt
W każdym branch-u dopasowany do potrzeb, w głównym ustalmy minimum


templates
pliki szablonów stron *.html.j2 lub *.j2

static 
wiadomo js, css, scss

odpalenie serwera
python3 main.py