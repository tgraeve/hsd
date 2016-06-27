Dieses Projekt thematisiert Hass im Internet. Es hat zum Ziel, die Verbreitung von Hasskommentaren aufzuzeigen und greifbarer zu machen.
Das Projekt holt Hatespeech aus dem Internet in die Realität, indem es dessen Ursprünge auf einer Karte verzeichnet. Diese Art der Visalisierung soll dem Nutzer einen Informationsgewinn bringen, in dem aufgezeigt wird, was in seinem geografischen Umfeld im Internet passiert.
Es beschränkt sich geografisch auf Deutschland und sprachlich auf die deutsche Sprache.


## Konzept

![Pipeline](/media/concept/pipeline_konzept.png "Pipeline Konzept")

1. Datenquelle
2. Datensammlung und -verarbeitung
3. Präsentation

### Datenquelle

Daten für unsere Anwendung müssen textueller Natur sein; hier bieten sich Kommentare und Posts in sozialen Netzwerken an. Für das anschließende Mapping muss den jeweiligen Aussagen ein geografischer Bezug zuzuordnen sein.

Als Datenquelle dient uns Twitter. Anfängliche Überlegungen zu Facebook, Youtube oder Reddit als Plattformen haben wir aus unterschiedlichsten Gründen verworfen. Hauptgrund für die Entscheidung für Twitter ist die größere Dichte an Geodaten zu den jeweiligen Aussagen und der simplere Aufbau des Netzwerkes. Tweets ordnen sich maximal durch Hashtags bestimmten Themen zu und müssen nicht aus Gruppen etc. extrahiert werden.


### Datensammlung und -verarbeitung

Twitter lässt durch seine [Search API](https://dev.twitter.com/rest/public/search) einen beschränkten Zugriff auf seine Daten zu.

Für den Zugriff und die Koordination der Abfragen greifen wir auf [Tweepy](http://tweepy.org) zurück.

Aktuell sammeln wir Tweets nach bestimmten Hashtags und speichern diese in JSON-Form zwischen. Die Hashtags sind Themen wie z.B. Homophobie zugeordnet und wurden anfangs händisch und intuitiv ausgewählt um dann nach und nach erweitert zu werden. Die Suchanfrage umschließt nur Tweets, welche Geodaten enthalten und welche zudem in Deutschland liegen müssen.

Wir erhoffen uns im Laufe des Projekts aus den gesammelten Daten weitere Erkenntnisse, die eine erweiterte Analyse von Tweets ermöglichen um die anfängliche Suche nach statischen Hashtags weiterentwickeln zu können.

Geplant ist, die so entstehende Menge an Tweets für unsere Zwecke vorerst händisch als Hatespeech zu klassifizieren, um eine Repräsentation auf Kartenebene zu ermöglichen.


### Präsentation

Das finale „Produkt“ wird eine frei zugängliche Website (voraussichtlich deutschlandhasst.de) sein, auf welcher der Endnutzer Tweets zu bestimmten HateSpeech-Themen visuell auf einer Landkarte angezeigt bekommt (Heatmap).

Der Nutzer kann hierbei die Darstellung wie folgt manipulieren:
- Bildausschnitt kann durch mehrstufigen Zoom und Verschiebung frei gewählt werden (die Cluster der Tweets werden beim hereinzoomen detaillierter und beim herauszoomen allgemeiner)
- Durch Checkboxen kann der Nutzer Themen oder auch einzelne Hashtags wählen, zu welchen die entsprechenden Tweets dargestellt werden sollen
- Über einen Slider kann der Nutzer den Zeitraum bestimmen, aus welchem die entsprechenden Tweets dargestellt werden sollen

Abbildung 1 zeigt den groben Aufbau, welchen wir uns für die Website vorstellen. Das Design kann und wird im Laufe des Projekts wahrscheinlich abweichen. Auch halten wir uns die Option offen, die Checkboxen durch Dropdown-Menüs zu ersetzen, falls die Darstellung durch die Menge der Auswahlmöglichkeiten zu unübersichtlich wird.

![Mockup](/media/concept/mockup1.png "Abbildung 1")


Zur technischen Realisierung der Präsentation nutzen wir die JavaScript-Bibliothek [OpenLayers](http://openlayers.org). Hierbei handelt es sich um eine JavaScript-API, die es ermöglicht, dynamische Karten auf Webseiten darzustellen.

In letzter Instanz mussten wir uns zunächst zwischen der [Google Maps API]http://(developers.google.com/maps/) und OpenLayers entscheiden, welche in ihrer Funktionalität sehr ähnlich sind.

Unsere Entscheidung fiel aus folgenden Gründen auf OpenLayers:
- Open Source
- In den Punkten Design und Funktionalität wesentlich flexibler als Google Maps
  - Quelle der Kartendaten kann frei gewählt werden
  - Eigene Features können leichter implementiert werden


