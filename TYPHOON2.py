import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import ttk, scrolledtext
import folium
import subprocess
import re
import sys
import time
import sv_ttk
from bs4 import BeautifulSoup
import requests

fenetre = tk.Tk()
sv_ttk.set_theme("dark")
fenetre.title("TYPH00n ©️ v1.0")
#fenetre.tk.call('source', 'forest-light.tcl')
#fenetre.Style().theme_use('forest-light')
####
# script results.txt
# ./dump1090 --interactive --net

texte_resultat = tk.Text(fenetre, wrap=tk.WORD, state="disabled", height=10, width=40)
texte_resultat.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


def overlay_typh(): ### START DUMP1090
    try:
        typh_result = """
   -               -           PRIVATE & RESTRICTED USAGE ONLY !
  -  -           -  -  
  - -  -  ---  -  - -     Welcome to TYPH00n ©️ (v2.0)
  -  -    ---    -  -   
   -     -- --     -     Framework for intercept
         -+ +-             ATC (Air-Traffic-Control) &
        - +++ -               ADSB (Automatic-Dependent-Surveillance–Broadcast) &
       --     --                 ACARS (Aircraft-Communication-Addressing-Reporting-System).
       -  +++  -      
      -++     ++-         This framework was developed for
     --++     ++--              research purposes in collaboration with SUPERPOSE INTELLIGENCE.
   -----------------               
"""
        #typh_result = subprocess.check_output(["ipconfig"], universal_newlines=True, shell=True)
        texte_resultat.config(state="normal")  # Activer la zone de texte
        texte_resultat.delete(1.0, tk.END)  # Effacer le contenu actuel
        texte_resultat.insert(tk.END, typh_result)  # Afficher le résultat dans la zone de texte
        texte_resultat.config(state="disabled")  # Désactiver la zone de texte
    except subprocess.CalledProcessError as e:
        texte_resultat.config(state="normal")  # Activer la zone de texte
        texte_resultat.delete(1.0, tk.END)  # Effacer le contenu actuel
        texte_resultat.insert(tk.END, f"Erreur : {e.returncode}\n{e.output}")  # Afficher l'erreur dans la zone de texte
        texte_resultat.config(state="disabled")  # Désactiver la zone de texte

overlay_typh()



# Fonction appelée lorsque le bouton "INTERCEPT" dans l'onglet "Principal" est cliqué
def executer_programme(): ### START DUMP1090
    try:
        # Exécuter un programme Python externe (par exemple, un fichier script.py)
        #result1 = subprocess.check_output(["script", " results.txt"], universal_newlines=True, shell=True)

        #result = subprocess.check_output(["route", "print"], universal_newlines=True, shell=True)
        result = subprocess.check_output(["screen", "./dump1090", "--interactive --net"], universal_newlines=True, shell=True)
        
        texte_resultat.config(state="normal")  # Activer la zone de texte
        texte_resultat.delete(1.0, tk.END)  # Effacer le contenu actuel
        texte_resultat.insert(tk.END, result)  # Afficher le résultat dans la zone de texte
        texte_resultat.config(state="disabled")  # Désactiver la zone de texte
    except subprocess.CalledProcessError as e:
        texte_resultat.config(state="normal")  # Activer la zone de texte
        texte_resultat.delete(1.0, tk.END)  # Effacer le contenu actuel
        texte_resultat.insert(tk.END, f"Erreur : {e.returncode}\n{e.output}")  # Afficher l'erreur dans la zone de texte
        texte_resultat.config(state="disabled")  # Désactiver la zone de texte

#def extract_coords(texte):
    # Utilisez une expression régulière pour rechercher des coordonnées GPS
#    coord_regex = r"(-?\d+\.\d+),\s*(-?\d+\.\d+)"
#    coordonnees = re.findall(coord_regex, texte)
#    return [(float(lat), float(lon)) for lat, lon in coordonnees]

#def extraire_coordonnees():
#    find_coords = texte_resultat.get(1.0, tk.END)  # Récupérer tout le contenu de la zone de texte
#    coordonnees = re.findall(r"(\d+\.\d+),\s*(-?\d+\.\d+)", find_coords)  # Utiliser une expression régulière pour trouver les coordonnées (format : 12.3456, -78.9012)

#    if coordonnees:
#        # Afficher les coordonnées trouvées
#        for lat, lon in coordonnees:
#            print(f"Latitude : {lat}, Longitude : {lon}")
#    else:
#        print("Aucune coordonnée GPS trouvée dans le texte.")

# Fonction appelée lorsque le bouton "Écouter" dans l'onglet "Listen" est cliqué
def bouton_listen_clic():

    option_select = liste_options.get(tk.ACTIVE)

    if option_select == "(Orly) LFPO TOWER - PARIS FRANCE":
        url = "https://www.liveatc.net/hlisten.php?icao=lfpo&mount=lfpo3_twr"
    elif option_select == "(Orly) LFPO DEPARTURE - PARIS FRANCE":
        url = "https://www.liveatc.net/hlisten.php?icao=lfpo&mount=lfpo_dep"
    elif option_select == "(Orly) LFPO APPROACH - PARIS FRANCE":
        url = "https://www.liveatc.net/hlisten.php?mount=lfpo3_app&icao=lfpo"
    elif option_select == "KJFK Tower - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?icao=kjfk&mount=kjfk_twr"
    elif option_select == "NY Departure (JFK) - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?mount=kjfk_dep"
    elif option_select == "ARINC (JFK/LGA Area) - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?icao=kjfk&mount=kjfk_arinc"
    elif option_select == "NY Approach (CAMRN/JFK) #3 - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?mount=kjfk_app_camrn"
    elif option_select == "NY Approach (ROBER/JFK #2) - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?icao=kjfk&mount=kjfk_app_rober"
    elif option_select == "NY Approach (Final/JFK) #2 - New York, New York, United States":
        url = "https://www.liveatc.net/hlisten.php?mount=kjfk_app_final&icao=kjfk"

    ### LFMN NICE AIRPORT
    elif option_select == "LFMN Ground/Tower - Nice, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfmn_twr"   
    elif option_select == "LFMN Approach - Nice, France":
        url = "https://www.liveatc.net/hlisten.php?icao=lfmn&mount=lfmn2"
    elif option_select == "LFMN Control (High) - Nice, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfmn2_m_high1"

    ### LFBD BORDEAUX AIRPORT
    elif option_select == "Bordeaux Control - Bordeaux, France":
        url = "https://www.liveatc.net/hlisten.php?icao=lfbd&mount=lfbd_bordeaux"   
    elif option_select == "LFBD Aquitane Approach - Bordeaux, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbd2_app&icao=lfbd"
    elif option_select == "LFBD Ground - Bordeaux, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbd2_gnd&icao=lfbd"
    elif option_select == "LFBD Tower - Bordeaux, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbd2_twr&icao=lfbd"

    ### LFBU LIMOGES AIRPORT
    elif option_select == "LFBU/LFBL Tower - Limoges, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbu"

    ### LFBU ANGOULEME
    elif option_select == "LFBU/LFBL Tower - Angouleme, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbu&icao=lfbu"
    elif option_select == "Bordeaux Control - Angouleme, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbd_bordeaux&icao=lfbu"

    ### LFBU ANGOULEME
    elif option_select == "LFBZ Tower - Biarritz, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbz2"



    elif option_select == "LFLP Twr/LFLB App - Annecy, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lflp"
    elif option_select == "LFLY Tower - Bron, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfly_twr"
    elif option_select == "LFST Emergency/Guard - Strasbourg, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfst_emergency"
    elif option_select == "LFST Approach #2 - Strasbourg, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfst_app2"
    elif option_select == "LFST Approach #1 - Strasbourg, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfst_app1"
    elif option_select == "LFMN FIS/Approach - Nice, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfmn_app2"
    elif option_select == "LFST Ground - Strasbourg, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfst_gnd"
    elif option_select == "Lyon FIS - Lyon, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfll2"
    elif option_select == "LFMD Ground/Tower - Cannes, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfmd_twr2"
    elif option_select == "Bordeaux Control - Bordeaux, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfbd_bordeaux"
    elif option_select == "LFST Tower - Strasbourg, France":
        url = "https://www.liveatc.net/hlisten.php?mount=lfst_twr"

    else:
        # Si une option inconnue est sélectionnée, ne rien faire
        return

    # Ouvrir l'URL dans un navigateur web
    webbrowser.open(url)

def enregistrer_contenu():
    contenu = texte_resultat.get(1.0, tk.END)
    with open("resultat.txt", "w") as fichier:
        fichier.write(contenu)


def bouton_map_clic():
    # Coordonnées de Paris
    latitude = 48.8588443
    longitude = 2.2943506

    webbrowser.open("http://localhost:8080")
    carte = folium.Map(location=[latitude, longitude], zoom_start=12, tiles="http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}",
                      attr="Google")
    
    ################################################################################
    ### CDG CHARLES DE GAULLE

    cdg_latitude = 49.0083899664
    cdg_longitude = 2.53844117956
    cdg_logo_html = '<div><img src="cdg_logo.png" alt="CDG" width="60" style="background-color: orange;"></div>'
    cdg_infos_supplementaires = """
    <h4>Charles de Gaulle AIRPORT (CDG)</h4>
    <p>IATA CODE: CDG</p>
    <p>ICAO CODE: LFPG</p>
    <p>CITY: Roissy-en-France, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    cdg_marqueur = folium.Marker(
        location=[cdg_latitude, cdg_longitude],
        icon=folium.DivIcon(html=cdg_logo_html)
    )
    #cdg_popup = folium.Popup(infos_supplementaires, max_width=300)
    cdg_popup_content = f'{cdg_infos_supplementaires}'
    cdg_popup = folium.Popup(cdg_popup_content, max_width=300)

    cdg_popup.add_to(cdg_marqueur)
    cdg_marqueur.add_to(carte)

    ################################################################################


    ory_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?icao=lfpo&mount=lfpo3_twr\'">LISTEN LFPO TOWER</button>'
    ory_bouton_html2 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?icao=lfpo&mount=lfpo_dep\'">LISTEN LFPO DEPARTURE</button>'
    ory_bouton_html3 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfpo3_app&icao=lfpo\'">LISTEN LFPO APPROACH</button>'
    ory_latitude = 48.7262433 
    ory_longitude = 2.3652472 
    ory_logo_html = '<div><img src="ory_logo.png" alt="LFPO" width="60" style="background-color: magenta;"></div>'
    ory_infos_supplementaires = """
    <h4>Orly AIRPORT (ORY)</h4>
    <p>IATA CODE: ORY</p>
    <p>ICAO CODE: LFPO</p>
    <p>CITY: Paris-Orly, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    ory_marqueur = folium.Marker(
        location=[ory_latitude, ory_longitude],
        icon=folium.DivIcon(html=ory_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    ory_popup_content = f'{ory_infos_supplementaires}<br>{ory_bouton_html}<br>{ory_bouton_html2}<br>{ory_bouton_html3}'
    ory_popup = folium.Popup(ory_popup_content, max_width=300)

    ory_popup.add_to(ory_marqueur)
    ory_marqueur.add_to(carte)

    ################################################################################


    fklk_latitude = 41.501
    fklk_longitude = 9.098
    fklk_logo_html = '<div><img src="fklk_logo.png" alt="FKLK" width="60" style="background-color: orange;"></div>'
    fklk_infos_supplementaires = """
    <h4>Figari AIRPORT (FSC)</h4>
    <p>IATA CODE: FSC</p>
    <p>ICAO CODE: FKLK</p>
    <p>CITY: Figari-Sud, Corse</p>
    <p>AIRPORT TYPE: International</p>
    """
    fklk_marqueur = folium.Marker(
        location=[fklk_latitude, fklk_longitude],
        icon=folium.DivIcon(html=fklk_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    fklk_popup_content = f'{fklk_infos_supplementaires}'
    fklk_popup = folium.Popup(fklk_popup_content, max_width=300)

    fklk_popup.add_to(fklk_marqueur)
    fklk_marqueur.add_to(carte)

    ################################################################################



    lfrk_latitude = 49.183333333333
    lfrk_longitude = -0.45
    lfrk_logo_html = '<div><img src="lfrk_logo.png" alt="LFRK" width="60" style="background-color: orange;"></div>'
    lfrk_infos_supplementaires = """
    <h4>Carpiquet AIRPORT (CFR)</h4>
    <p>IATA CODE: CFR</p>
    <p>ICAO CODE: LFRK</p>
    <p>CITY: Caen-Carpiquet, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfrk_marqueur = folium.Marker(
        location=[lfrk_latitude, lfrk_longitude],
        icon=folium.DivIcon(html=lfrk_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfrk_popup_content = f'{lfrk_infos_supplementaires}'
    lfrk_popup = folium.Popup(lfrk_popup_content, max_width=300)

    lfrk_popup.add_to(lfrk_marqueur)
    lfrk_marqueur.add_to(carte)

    ################################################################################


    lfbd_latitude = 44.8291
    lfbd_longitude = -0.702779
    lfbd_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?icao=lfbd&mount=lfbd_bordeaux\'">LISTEN LFBD CONTROL</button>'
    lfbd_bouton_html2 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbd2_app&icao=lfbd\'">LISTEN LFBD AQUITAINE APPROACH</button>'
    lfbd_bouton_html3 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbd2_gnd&icao=lfbd\'">LISTEN LFBD GROUND</button>'
    lfbd_bouton_html4 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbd2_twr&icao=lfbd\'">LISTEN LFBD TOWER</button>'
    lfbd_logo_html = '<div><img src="lfbd_logo.png" alt="LFBD" width="60" style="background-color: magenta;"></div>'
    lfbd_infos_supplementaires = """
    <h4>Bordeaux AIRPORT (LFBD)</h4>
    <p>IATA CODE: BOD</p>
    <p>ICAO CODE: LFBD</p>
    <p>CITY: Merignac-Bordeaux, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfbd_marqueur = folium.Marker(
        location=[lfbd_latitude, lfbd_longitude],
        icon=folium.DivIcon(html=lfbd_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfbd_popup_content = f'{lfbd_infos_supplementaires}<br>{lfbd_bouton_html}<br>{lfbd_bouton_html2}<br>{lfbd_bouton_html3}<br>{lfbd_bouton_html4}'
    lfbd_popup = folium.Popup(lfbd_popup_content, max_width=300)

    lfbd_popup.add_to(lfbd_marqueur)
    lfbd_marqueur.add_to(carte)

    ################################################################################

    lfbu_latitude = 45.7292
    lfbu_longitude = 0.22146
    lfbu_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbu\'">LISTEN LFBU/LFBL TOWER</button>'
    lfbu_logo_html = '<div><img src="lfbu_logo.png" alt="LFBU" width="60" style="background-color: magenta;"></div>'
    lfbu_infos_supplementaires = """
    <h4>Cognac FIR AIRPORT (LFBU)</h4>
    <p>IATA CODE: ANG</p>
    <p>ICAO CODE: LFBU</p>
    <p>CITY: Angoulême-Brie-Champniers, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfbu_marqueur = folium.Marker(
        location=[lfbu_latitude, lfbu_longitude],
        icon=folium.DivIcon(html=lfbu_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfbu_popup_content = f'{lfbu_infos_supplementaires}<br>{lfbu_bouton_html}'
    lfbu_popup = folium.Popup(lfbu_popup_content, max_width=300)

    lfbu_popup.add_to(lfbu_marqueur)
    lfbu_marqueur.add_to(carte)

    ################################################################################


    lfbl_latitude = 45.86300
    lfbl_longitude = 1.18300
    lfbl_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbu\'">LISTEN LFBU/LFBL TOWER</button>'
    lfbl_logo_html = '<div><img src="lfbl_logo.png" alt="LFBL" width="60" style="background-color: magenta;"></div>'
    lfbl_infos_supplementaires = """
    <h4>Bellegarde AIRPORT (LFBL)</h4>
    <p>IATA CODE: LIG</p>
    <p>ICAO CODE: LFBL</p>
    <p>CITY: Limoges, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfbl_marqueur = folium.Marker(
        location=[lfbl_latitude, lfbl_longitude],
        icon=folium.DivIcon(html=lfbl_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfbl_popup_content = f'{lfbl_infos_supplementaires}<br>{lfbl_bouton_html}'
    lfbl_popup = folium.Popup(lfbl_popup_content, max_width=300)

    lfbl_popup.add_to(lfbl_marqueur)
    lfbl_marqueur.add_to(carte)

    ################################################################################

    lfbz_latitude = 43.46833
    lfbz_longitude = -1.53111
    lfbz_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfbz2\'">LISTEN LFBZ TOWER</button>'
    lfbz_logo_html = '<div><img src="lfbz_logo.png" alt="LFBZ" width="60" style="background-color: magenta;"></div>'
    lfbz_infos_supplementaires = """
    <h4>Bayonne AIRPORT (LFBZ)</h4>
    <p>IATA CODE: BIQ</p>
    <p>ICAO CODE: LFBZ</p>
    <p>CITY: Biarritz-Anglet-Bayonne, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfbz_marqueur = folium.Marker(
        location=[lfbz_latitude, lfbz_longitude],
        icon=folium.DivIcon(html=lfbz_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfbz_popup_content = f'{lfbz_infos_supplementaires}<br>{lfbz_bouton_html}'
    lfbz_popup = folium.Popup(lfbz_popup_content, max_width=300)

    lfbz_popup.add_to(lfbz_marqueur)
    lfbz_marqueur.add_to(carte)

    ################################################################################


    lfll_latitude = 45.72556
    lfll_longitude = 5.08111
    lfll_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfll\'">LISTEN LFLL TOWER</button>'
    lfll_logo_html = '<div><img src="lfll_logo.png" alt="LFLL" width="60" style="background-color: magenta;"></div>'
    lfll_infos_supplementaires = """
    <h4>Lyon AIRPORT (LFLL)</h4>
    <p>IATA CODE: LYS</p>
    <p>ICAO CODE: LFLL</p>
    <p>CITY: Lyon, France</p>
    <p>REGION: Auvergne-Rhône-Alpes</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfll_marqueur = folium.Marker(
        location=[lfll_latitude, lfll_longitude],
        icon=folium.DivIcon(html=lfll_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfll_popup_content = f'{lfll_infos_supplementaires}<br>{lfll_bouton_html}'
    lfll_popup = folium.Popup(lfll_popup_content, max_width=300)

    lfll_popup.add_to(lfll_marqueur)
    lfll_marqueur.add_to(carte)

    ################################################################################


    lflp_latitude = 45.92900
    lflp_longitude = 6.10000
    lflp_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lflp\'">LISTEN LFLP TOWER/LFLB APP</button>'
    lflp_logo_html = '<div><img src="lflp_logo.png" alt="LFLP" width="60" style="background-color: magenta;"></div>'
    lflp_infos_supplementaires = """
    <h4>Meythet AIRPORT (LFLP)</h4>
    <p>IATA CODE: NCY</p>
    <p>ICAO CODE: LFLP</p>
    <p>CITY: Annecy, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lflp_marqueur = folium.Marker(
        location=[lflp_latitude, lflp_longitude],
        icon=folium.DivIcon(html=lflp_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lflp_popup_content = f'{lflp_infos_supplementaires}<br>{lflp_bouton_html}'
    lflp_popup = folium.Popup(lflp_popup_content, max_width=300)

    lflp_popup.add_to(lflp_marqueur)
    lflp_marqueur.add_to(carte)

    ################################################################################



    lfly_latitude = 45.724330436
    lfly_longitude = 4.93666292
    lfly_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfly_twr\'">LISTEN LFLY TOWER</button>'
    lfly_logo_html = '<div><img src="lfly_logo.png" alt="LFLY" width="60" style="background-color: magenta;"></div>'
    lfly_infos_supplementaires = """
    <h4>Bron AIRPORT (LFLY)</h4>
    <p>IATA CODE: LYN</p>
    <p>ICAO CODE: LFLY</p>
    <p>CITY: Bron, France</p>
    <p>REGION: Auvergne-Rhône-Alpes</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfly_marqueur = folium.Marker(
        location=[lfly_latitude, lfly_longitude],
        icon=folium.DivIcon(html=lfly_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfly_popup_content = f'{lfly_infos_supplementaires}<br>{lfly_bouton_html}'
    lfly_popup = folium.Popup(lfly_popup_content, max_width=300)

    lfly_popup.add_to(lfly_marqueur)
    lfly_marqueur.add_to(carte)

    ################################################################################



    lfst_latitude = 48.5383
    lfst_longitude = 7.62823
    lfst_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfst_emergency\'">LISTEN LFST EMERGENCY/GUARD</button>'
    lfst_bouton_html2 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfst_app1\'">LISTEN LFST APPROACH #1</button>'
    lfst_bouton_html3 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfst_app2\'">LISTEN LFST APPROACH #2</button>'
    lfst_bouton_html4 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfst_gnd\'">LISTEN LFST GROUND</button>'
    lfst_bouton_html5 = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfst_twr\'">LISTEN LFST CONTROL TOWER</button>'
    lfst_logo_html = '<div><img src="lfst_logo.png" alt="LFST" width="60" style="background-color: magenta;"></div>'
    lfst_infos_supplementaires = """
    <h4>Strasbourg Entzheim AIRPORT (LFST)</h4>
    <p>IATA CODE: SXB</p>
    <p>ICAO CODE: LFST</p>
    <p>CITY: Strasbourg, France</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfst_marqueur = folium.Marker(
        location=[lfst_latitude, lfst_longitude],
        icon=folium.DivIcon(html=lfst_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfst_popup_content = f'{lfst_infos_supplementaires}<br>{lfst_bouton_html}<br>{lfst_bouton_html2}<br>{lfst_bouton_html3}<br>{lfst_bouton_html4}<br>{lfst_bouton_html5}'
    lfst_popup = folium.Popup(lfst_popup_content, max_width=300)

    lfst_popup.add_to(lfst_marqueur)
    lfst_marqueur.add_to(carte)

    ################################################################################


    lfmn_latitude = 43.6584
    lfmn_longitude = 7.21587
    lfmn_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfly_twr\'">LISTEN FIS APPROACH</button>'
    lfmn_logo_html = '<div><img src="lfmn_logo.png" alt="LFMN" width="60" style="background-color: magenta;"></div>'
    lfmn_infos_supplementaires = """
    <h4>Nice AIRPORT (LFMN)</h4>
    <p>IATA CODE: NCE</p>
    <p>ICAO CODE: LFMN</p>
    <p>CITY: Saint-Laurent-du-Var, France</p>
    <p>REGION: Provence-Alpes-Côte d'Azur</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfmn_marqueur = folium.Marker(
        location=[lfmn_latitude, lfmn_longitude],
        icon=folium.DivIcon(html=lfmn_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfmn_popup_content = f'{lfmn_infos_supplementaires}<br>{lfmn_bouton_html}'
    lfmn_popup = folium.Popup(lfmn_popup_content, max_width=300)

    lfmn_popup.add_to(lfmn_marqueur)
    lfmn_marqueur.add_to(carte)

    ################################################################################


    lfmd_latitude = 43.542
    lfmd_longitude = 6.95348
    lfmd_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=lfly_twr\'">LISTEN LFMD GROUND/TOWER</button>'
    lfmd_logo_html = '<div><img src="lfmd_logo.png" alt="LFMD" width="60" style="background-color: magenta;"></div>'
    lfmd_infos_supplementaires = """
    <h4>Cannes-Mandelieu AIRPORT (LFMD)</h4>
    <p>IATA CODE: CEQ</p>
    <p>ICAO CODE: LFMD</p>
    <p>CITY: Mandelieu-la-Napoule, France</p>
    <p>REGION: Provence-Alpes-Côte d'Azur</p>
    <p>AIRPORT TYPE: International</p>
    """
    lfmd_marqueur = folium.Marker(
        location=[lfmd_latitude, lfmd_longitude],
        icon=folium.DivIcon(html=lfmd_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    lfmd_popup_content = f'{lfmd_infos_supplementaires}<br>{lfmd_bouton_html}'
    lfmd_popup = folium.Popup(lfmd_popup_content, max_width=300)

    lfmd_popup.add_to(lfmd_marqueur)
    lfmd_marqueur.add_to(carte)

    ################################################################################


    uuee_latitude = 55.9726
    uuee_longitude = 37.4146
    uuee_bouton_html = '<button onclick="window.location.href=\'https://www.liveatc.net/hlisten.php?mount=uuee3&icao=uuee\'">LISTEN UUEE TOWER/APP/RADAR</button>'
    uuee_logo_html = '<div><img src="uuee_logo.png" alt="UUEE" width="60" style="background-color: magenta;"></div>'
    uuee_infos_supplementaires = """
    <h4>Sheremetyevo AIRPORT (LFMD)</h4>
    <p>IATA CODE: SVO</p>
    <p>ICAO CODE: UUEE</p>
    <p>CITY: Isakovo, Russia</p>
    <p>REGION: Moscow Oblast</p>
    <p>AIRPORT TYPE: International</p>
    """
    uuee_marqueur = folium.Marker(
        location=[uuee_latitude, uuee_longitude],
        icon=folium.DivIcon(html=uuee_logo_html)
    )
    #ory_popup = folium.Popup(infos_supplementaires, max_width=300)
    uuee_popup_content = f'{uuee_infos_supplementaires}<br>{uuee_bouton_html}'
    uuee_popup = folium.Popup(uuee_popup_content, max_width=300)

    uuee_popup.add_to(uuee_marqueur)
    uuee_marqueur.add_to(carte)

    ################################################################################

    # Créer un menu OSM personnalisé
    folium.TileLayer("OpenStreetMap").add_to(carte)  # Ajouter la couche OSM d'origine
    folium.TileLayer("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", attr="Google").add_to(carte)  # Ajouter la couche Google Satellite
    folium.TileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", attr="OpenStreetMap").add_to(carte)  # Ajouter la couche OSM
        
    # Ajouter un contrôle de changement de couche (original ou satellite) au menu OSM
    folium.LayerControl(position='topright', collapsed=False).add_to(carte)




    # Sauvegarder la carte dans un fichier HTML temporaire
    carte.save("25_crosshair_5.html")

    # Ouvrir la carte dans le navigateur par défaut
    webbrowser.open("25_crosshair_5.html")







# Créer une fenêtre Tkinter avec les dimensions spécifiées
#fenetre = tk.Tk()
#sv_ttk.set_theme("dark")
#fenetre.tk.call('source', 'forest-light.tcl')
#fenetre.Style().theme_use('forest-light')


#fenetre.title("TYPH00N ©️ v1.0")
fenetre.geometry("1280x600")  # Dimensions de la fenêtre : 800x300
fenetre.configure(bg="#202c38")
fenetre.wm_iconbitmap('assets/718378.ico')

# Créer une barre d'outils dans l'onglet "Principal"
barre_outils_principal = tk.Menu(fenetre)
barre_outils_principal.configure(bg="#202c38")    
fenetre.config(menu=barre_outils_principal)

# Menu Fichier dans l'onglet "Principal"
menu_fichier_principal = tk.Menu(barre_outils_principal, tearoff=0)
menu_fichier_principal.configure(bg="#272a30")                                              ### COULEUR
barre_outils_principal.add_cascade(label="Files", menu=menu_fichier_principal)
menu_fichier_principal.add_command(label="DUMP", command=executer_programme)
menu_fichier_principal.add_command(label="SAVE", command=enregistrer_contenu)
menu_fichier_principal.add_separator()
menu_fichier_principal.add_command(label="Quitter", command=fenetre.quit)




# Créer une zone de texte pour afficher le résultat et placer-la à gauche dans l'onglet "Principal"
#texte_resultat = tk.Text(fenetre, wrap=tk.WORD, state="disabled", height=10, width=40)
#texte_resultat.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Créer un bouton "INTERCEPT" pour exécuter le programme et placer-le à droite dans l'onglet "Principal"

credit_button = tk.Button(fenetre, text="INFOS", command=executer_programme) 
credit_button.grid(row=0, column=3, padx=10, pady=10, sticky="n")

bouton_executer = tk.Button(fenetre, text="DUMP", command=executer_programme) 
bouton_executer.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Bouton "SAVE" pour enregistrer le contenu
bouton_save = tk.Button(fenetre, text="SAVE", command=enregistrer_contenu)
bouton_save.grid(row=0, column=2, padx=10, pady=10, sticky="n")

# Configurer la gestion de la grille pour les proportions dans l'onglet "Principal"
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_columnconfigure(0, weight=1)

# Créer un notebook (onglet) pour organiser le contenu
notebook = ttk.Notebook(fenetre)
notebook.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# ACAR DECODER
acars_decoder = ttk.Frame(notebook)
notebook.add(acars_decoder, text="ACARS")

# Onglet "Listen"
onglet_listen = ttk.Frame(notebook)
notebook.add(onglet_listen, text="ATC")

onglet_map = ttk.Frame(notebook)
notebook.add(onglet_map, text="ADSB")


onglet_arrivals = ttk.Frame(notebook)
notebook.add(onglet_arrivals, text="ARRIVALS")

arr_iata_search = tk.Entry(onglet_arrivals, width=20)  # Ajustez la largeur selon vos besoins
arr_iata_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Positionné à gauche

arr_result_text = tk.Text(onglet_arrivals, height=5, width=80)
arr_result_text.grid(row=2, column=0, padx=10, pady=10, sticky="w")

def dump_arr():
    icao_code = arr_iata_search.get().upper()
    if len(icao_code) == 4:
        url = f"https://www.radarbox.com/data/airports/{icao_code}?tab=arrivals"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Trouver tous les éléments avec la classe dynamique
            elements = soup.find_all(class_=lambda x: x and 'sc-7jy3gr-3' in x.split())

            # Créer une nouvelle fenêtre pour afficher les éléments
            display_window = tk.Toplevel(fenetre)
            display_window.title(f"ARRIVALS {icao_code}")

            # Créer une zone de texte élastique pour afficher les résultats
            display_text = scrolledtext.ScrolledText(display_window, wrap=tk.WORD, width=80, height=20)
            display_text.pack(expand=True, fill='both')

            def update_results():
                display_text.delete(1.0, tk.END)  # Effacer le contenu actuel
                for element in elements:
                    divs_with_id = element.find_all("tr", id=True)
                    if divs_with_id:
                        for div_with_id in divs_with_id:
                            display_text.insert(tk.END, div_with_id.text + '\n')
                    else:
                        display_text.insert(tk.END, "Aucune balise div avec un attribut id trouvé.\n")

                # Planifier la prochaine mise à jour après un certain délai (en millisecondes)
                display_window.after(50, update_results)  # Mettez à jour toutes les 5000 millisecondes (5 secondes)

            # Lancer la première actualisation
            update_results()
        else:
            # Afficher une erreur si la requête HTTP échoue
            arr_result_text.delete(1.0, tk.END)
            arr_result_text.insert(tk.END, f"Erreur de requête HTTP: {response.status_code}")
    else:
        # Afficher un message si le code ICAO n'est pas valide
        arr_result_text.delete(1.0, tk.END)
        arr_result_text.insert(tk.END, "Veuillez entrer un code ICAO valide composé de 4 lettres.")

arr_submit_button = tk.Button(onglet_arrivals, text="TRACK ARRIVALS", command=dump_arr)
arr_submit_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")





onglet_departures = ttk.Frame(notebook)
notebook.add(onglet_departures, text="DEPARTURES")

dep_iata_search = tk.Entry(onglet_departures, width=20)  # Ajustez la largeur selon vos besoins
dep_iata_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Positionné à gauche

dep_result_text = tk.Text(onglet_departures, height=5, width=80)
dep_result_text.grid(row=2, column=0, padx=10, pady=10, sticky="w")

def dump_dep():
    icao_code = dep_iata_search.get().upper()
    if len(icao_code) == 4:
        url = f"https://www.radarbox.com/data/airports/{icao_code}?tab=departures"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Trouver tous les éléments avec la classe dynamique
            elements = soup.find_all(class_=lambda x: x and 'sc-1stzqh5-0' in x.split())

            # Créer une nouvelle fenêtre pour afficher les éléments
            display_window = tk.Toplevel(fenetre)
            display_window.title(f"DEPARTURES {icao_code}")

            # Créer une zone de texte élastique pour afficher les résultats
            display_text = scrolledtext.ScrolledText(display_window, wrap=tk.WORD, width=80, height=20)
            display_text.pack(expand=True, fill='both')

            def update_results():
                display_text.delete(1.0, tk.END)  # Effacer le contenu actuel
                for element in elements:
                    divs_with_id = element.find_all("tr", id=True)
                    if divs_with_id:
                        for div_with_id in divs_with_id:
                            display_text.insert(tk.END, div_with_id.text + '\n')
                    else:
                        display_text.insert(tk.END, "Aucune balise div avec un attribut id trouvé.\n")

                # Planifier la prochaine mise à jour après un certain délai (en millisecondes)
                display_window.after(50, update_results)  # Mettez à jour toutes les 5000 millisecondes (5 secondes)

            # Lancer la première actualisation
            update_results()
        else:
            # Afficher une erreur si la requête HTTP échoue
            dep_result_text.delete(1.0, tk.END)
            dep_result_text.insert(tk.END, f"Erreur de requête HTTP: {response.status_code}")
    else:
        # Afficher un message si le code ICAO n'est pas valide
        dep_result_text.delete(1.0, tk.END)
        dep_result_text.insert(tk.END, "Veuillez entrer un code ICAO valide composé de 4 lettres.")

departures_submit_button = tk.Button(onglet_departures, text="TRACK DEPARTURES", command=dump_dep)
departures_submit_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")



bouton_run_map = tk.Button(onglet_map, text="INTERACTIVE MAP", command=bouton_map_clic)
bouton_run_map.pack()
bouton_run_map.grid(row=1, column=1, padx=10, pady=10)

# Créer une zone de sélection (Listbox) dans l'onglet "Listen"
liste_options = tk.Listbox(onglet_listen, selectmode=tk.SINGLE, width=125)
liste_options.grid(row=1, column=0, padx=10, pady=10)




# Créer une zone de recherche (Entry) dans l'onglet "Listen"
recherche_entry = tk.Entry(onglet_listen, width=30)
recherche_entry.grid(row=0, column=0, padx=(6, 0), pady=10, sticky="w")

def mettre_a_jour_liste():
    mot_cle = recherche_entry.get().lower()  # Convertir le mot-clé en minuscules pour une recherche insensible à la casse
    liste_options.delete(0, tk.END)  # Effacer la liste actuelle

    # Ajouter les éléments correspondant au mot-clé
    for option in options:
        if mot_cle in option.lower():
            liste_options.insert(tk.END, option)

# Associer la fonction de mise à jour à l'événement de saisie dans la zone de recherche
recherche_entry.bind("<KeyRelease>", lambda event: mettre_a_jour_liste())

# Ajouter des options à la zone de sélection
options = ["(Orly) LFPO TOWER - PARIS FRANCE", "(Orly) LFPO DEPARTURE - PARIS FRANCE", "(Orly) LFPO APPROACH - PARIS FRANCE", "KJFK Tower - New York, New York, United States", "NY Departure (JFK) - New York, New York, United States", "ARINC (JFK/LGA Area) - New York, New York, United States", "NY Approach (CAMRN/JFK) #3 - New York, New York, United States", "NY Approach (ROBER/JFK #2) - New York, New York, United States", "NY Approach (Final/JFK) #2 - New York, New York, United States", "LFMN Ground/Tower - Nice, France", "LFMN Approach - Nice, France", "LFMN Control (High) - Nice, France", "Bordeaux Control - Bordeaux, France", "LFBD Aquitane Approach - Bordeaux, France", "LFBD Ground - Bordeaux, France", "LFBD Tower - Bordeaux, France", "LFBU/LFBL Tower - Limoges, France", "LFBU/LFBL Tower - Angouleme, France", "Bordeaux Control - Angouleme, France", "LFBZ Tower - Biarritz, France", "LFLP Twr/LFLB App - Annecy, France", "LFLY Tower - Bron, France", "LFST Emergency/Guard - Strasbourg, France", "LFST Approach #2 - Strasbourg, France", "LFST Approach #1 - Strasbourg, France", "LFMN FIS/Approach - Nice, France", "LFST Ground - Strasbourg, France", "Lyon FIS - Lyon, France", "LFMD Ground/Tower - Cannes, France", "Bordeaux Control - Bordeaux, France", "LFST Tower - Strasbourg, France"]
for option in options:
    liste_options.insert(tk.END, option)

# Ajouter un bouton "Écouter" à côté de la zone de sélection dans l'onglet "Listen"
bouton_listen = tk.Button(onglet_listen, text="LISTEN ATC", command=bouton_listen_clic)
bouton_listen.grid(row=0, column=0, padx=10, pady=10, sticky="n")





# Créer un libellé (Label) pour afficher le texte sélectionné
texte_selection_label = tk.Label(onglet_listen, text="ATC Selection :", foreground="green")
texte_selection_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Fonction pour mettre à jour le texte sélectionné
def mettre_a_jour_texte_selection(event):
    # Récupérer l'index de l'élément sélectionné
    index_selectionne = liste_options.curselection()

    # Vérifier si un élément est sélectionné
    if index_selectionne:
        texte_selection = liste_options.get(index_selectionne)
        texte_selection_label.config(text=f"ATC Selection : {texte_selection}")
    else:
        texte_selection_label.config(text="ATC Selection : Aucun")

# Associer la fonction de mise à jour à l'événement de sélection dans la Listbox
liste_options.bind("<<ListboxSelect>>", mettre_a_jour_texte_selection)



# Lancer la boucle principale Tkinter
fenetre.mainloop()
