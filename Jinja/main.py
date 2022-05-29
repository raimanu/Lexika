import jinja2
import csv

def creer_html(fichier_template, fichier_sortie, fichier_csv) :
  env= jinja2.Environment()
  env.loader= jinja2.FileSystemLoader("./")
  template= env.get_template( fichier_template )
  rdr= csv.reader( open(fichier_csv, "r" ) )
  csv_data = [ lines for lines in rdr ]
  html = template.render( data=csv_data )
  f = open(fichier_sortie, 'w')
  f.write(html)
  f.close()

creer_html("LEXIKA.html","test.html","select.csv")