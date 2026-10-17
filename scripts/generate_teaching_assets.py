"""Generate bilingual teaching sources, fictional data and reproducible plots.

Run with the project .venv. Requires matplotlib (requirements-figures.txt).
Render Graphviz sources afterwards with scripts/render_diagrams.py.
All example records, studies, passages and judgements are fictional.
"""
from pathlib import Path
import csv
import json
import zipfile
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
OUT=ROOT/'book/_static/downloads'
SRC=ROOT/'diagram_sources'
IMG=ROOT/'book/_static/generated/diagrams'
STUDIES=[
 ('S01','resident',24,'time;errors','yes','yes','yes'),
 ('S02','resident',18,'time','yes','unclear','yes'),
 ('S03','student',30,'errors;force','yes','yes','yes'),
 ('S04','student',16,'time;force','unclear','yes','yes'),
 ('S05','resident',22,'errors','yes','yes','unclear'),
 ('S06','student',20,'time;errors;force','yes','yes','yes'),
]
T={
 'es':dict(student='Estudiante',resident='Residente',time='Tiempo',errors='Errores',force='Fuerza',yes='Sí',unclear='No informado',title='Mapa de evidencia: seis estudios ficticios',x='Población',y='Métrica registrada',matrix='Evaluación crítica por dominios: ejemplo ficticio',domains=['Validez de\nla medida','Datos\nausentes','Contexto\ndescrito'],foot='Cada estudio puede aportar varias métricas. El área representa el número de estudios.',judgement='Sí = criterio documentado; NI = no informado. No es una escala validada.'),
 'en':dict(student='Student',resident='Resident',time='Time',errors='Errors',force='Force',yes='Yes',unclear='Not reported',title='Evidence map: six fictional studies',x='Population',y='Reported metric',matrix='Domain-level critical appraisal: fictional example',domains=['Measurement\nvalidity','Missing\ndata','Context\ndescribed'],foot='Each study may report several metrics. Area represents the number of studies.',judgement='Y = criterion documented; NR = not reported. This is not a validated scale.')}
def csvwrite(path,headers,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(headers);w.writerows(rows)
def mermaid(lang, name, body):
 # Keep compact flow specifications in this generator; export editable DOT.
 # Graphviz avoids remote Mermaid rendering and HTML-only SVG text.
 import re
 def quote(text):
  return json.dumps(text, ensure_ascii=False)
 lines=['digraph G {', 'graph [rankdir='+('LR' if 'flowchart LR' in body else 'TB')+', bgcolor="white", pad="0.25", nodesep="0.35", ranksep="0.45", fontname="Arial", fontsize=17];', 'node [shape=box, style="rounded,filled", fillcolor="#edf5fa", color="#277b9b", fontcolor="#163247", fontname="Arial", fontsize=17, margin="0.18,0.12"];', 'edge [color="#526e80", fontname="Arial", fontsize=13, arrowsize=0.7];']
 body=re.sub(r'subgraph (\w+)\["([^"\]]+)"\]', lambda m:'CLUSTER '+m[1]+' '+json.dumps(m[2],ensure_ascii=False),body)
 defs=[]
 def node(m):
  defs.append((m[1],m[3],m[2]=='{'))
  return m[1]
 body=re.sub(r'(\b[A-Z]\w*)(\[|\{)"([\s\S]*?)"(?:\]|\})',node,body)
 # Definitions first; membership is declared explicitly in each cluster below.
 for ident,label,diamond in defs:
  lines.append(ident+' [label='+quote(label)+(', shape=diamond' if diamond else '')+'];')
 in_cluster=False
 for raw in body.splitlines():
  line=raw.strip()
  if not line or line.startswith('flowchart'):continue
  if line.startswith('CLUSTER '):
   _,ident,label=line.split(' ',2);lines.append('subgraph cluster_'+ident+' { label='+label+'; color="#b7c9d5";');in_cluster=True;continue
  if line=='end':lines.append('}');in_cluster=False;continue
  edge=re.match(r'^(\w+)\s*(-->|-\.->|-\.\s*"([^"]+)"\s*\.->)\s*(?:\|([^|]+)\|)?\s*(\w+)$',line)
  if edge:
   attrs=[]
   if edge[3] or edge[4]:attrs.append('label='+quote(edge[3] or edge[4]))
   if edge[2].startswith('-.'):attrs.append('style=dashed')
   lines.append(edge[1]+' -> '+edge[5]+(' ['+', '.join(attrs)+']' if attrs else '')+';')
  elif re.fullmatch(r'\w+',line):lines.append(line+';')
  else:raise ValueError('Unsupported flow line: '+line)
 lines.append('}')
 p=SRC/lang/(name+'_'+lang+'.graphviz');p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
for lang in ('es','en'):
 es=lang=='es';d=OUT/lang;d.mkdir(parents=True,exist_ok=True)
 # 40 database records: 8 duplicate records, 32 screened, 22 excluded;
 # 10 sought, 1 unavailable, 9 assessed, 4 excluded, 5 included.
 # One citation-search report assessed and included: total 6 reports/studies.
 rows=[]
 for i in range(1,42):
  rid=f'R{i:02}'; report=f'P{i:02}' if i<=5 else f'P{100+i:03}'; study='';duplicate='';reason='';retrieved='';title_dec='';full=''
  origin='database' if i<=40 else 'citation_search'
  source=('Scopus' if i<=24 else 'IEEE Xplore') if i<=40 else 'snowballing'
  if i<=6: study=f'S{i:02}'; report=f'P{i:02}' if i<=5 else f'P{100+i:03}'; title_dec='include';retrieved='yes';full='include'
  if i==6: title_dec='exclude';retrieved='';full='';study='';reason='EC1_population'
  if 7<=i<=27:title_dec='exclude';reason='EC1_population' if i%2 else 'EC2_no_metric'
  if i==28:title_dec='include';retrieved='no';reason='not_retrieved'
  if 29<=i<=32:title_dec='include';retrieved='yes';full='exclude';reason='EC1_population' if i<=30 else 'EC2_no_metric'
  if 33<=i<=40:duplicate=f'R{i-32:02}';report=f'P{i-32:02}' if i-32<=5 else f'P{100+i-32:03}'
  if i==41:study='S06';report='P06';title_dec='not_applicable';retrieved='yes';full='include'
  rows.append([rid,report,study,source,origin,duplicate,title_dec,title_dec,full,retrieved,reason,'FICTITIOUS'])
 headers=['record_id','report_id','study_id','source','origin','duplicate_of','title_abstract_A','title_abstract_B','full_text_final','retrieved','reason','data_status']
 csvwrite(d/'screening_example.csv',headers,rows)
 csvwrite(d/'screening_template.csv',headers,[])
 extraction=[]
 for j,(sid,pop,n,metrics,*domains) in enumerate(STUDIES):
  extraction.append([sid,'P'+sid[1:],T[lang][pop],n,';'.join(T[lang][m] for m in metrics.split(';')),2,'A','2026-10-16',*[T[lang][v] for v in domains],'FICTITIOUS'])
 eh=['study_id','report_id','population','participants','metrics','source_page','reviewer','extraction_date','measurement_validity','missing_data','context','data_status']
 csvwrite(d/'extraction_example.csv',eh,extraction);csvwrite(d/'extraction_template.csv',eh,[])
 csvwrite(d/'search_log_template.csv',['source','platform','exact_query','fields','limits','search_date','results','export_file','notes'],[])
 csvwrite(d/'amendments_template.csv',['date','protocol_version','change','reason','stage','impact','approved_by'],[])
 csvwrite(d/'codebook.csv',['field','allowed_values','definition'],[
 ['population','student;resident','Final-year student or surgical resident; mutually exclusive in this exercise'],
 ['metrics','time;errors;force','Multiple categories allowed; absence of a category is not evidence of clinical ineffectiveness'],
 ['appraisal','yes;unclear','Documented criterion or not reported; illustrative domains, not a validated instrument']])
 counts={'database_records':40,'duplicate_records':8,'screened':32,'title_abstract_excluded':22,'reports_sought':10,'reports_not_retrieved':1,'reports_assessed':9,'full_text_excluded':4,'database_included':5,'citation_reports_assessed':1,'citation_reports_included':1,'included_reports':6,'included_studies':6}
 (d/'flow_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf-8')
 (d/'README.txt').write_text(('DATOS FICTICIOS PARA DOCENCIA. No representan estudios reales ni resultados de la revisión original.\n' if es else 'FICTIONAL TEACHING DATA. These are not real studies or results of the original review.\n')+'CC BY 4.0 - Daniel H. de la Iglesia, 2026.\nReproduce: .venv/Scripts/python.exe scripts/generate_teaching_assets.py\n'+('Columnas e identificadores estables en inglés para facilitar la reproducción; valores de extracción traducidos.\n' if es else 'Stable English column names and identifiers support reproducibility; extraction values are localised.\n')+'40 - 8 = 32; 32 - 22 = 10; 10 - 1 = 9; 9 - 4 = 5; 5 + 1 = 6.\n'+'The illustrative appraisal domains do not replace MMAT, RoB 2 or another validated instrument.\n',encoding='utf-8')
 assert sum(r[5]!='' for r in rows)==8
 assert sum(r[8]=='include' for r in rows)==6
 assert sum(r[8]=='exclude' for r in rows)==4
 assert len({r[2] for r in rows if r[2]})==6
 # Editable diagrams.
 mermaid(lang,'process', '''flowchart TB
 A["Pregunta y objetivo\nEntregable: RQ y alcance"] --> B["Protocolo revisado\nMétodos y registro de cambios"]
 B --> C["Búsqueda validada\nCadenas, fechas y exportaciones"]
 C --> D["Selección\nDecisiones y flujo PRISMA"]
 D --> E["Evaluación crítica y extracción\nJuicios y datos con página"]
 E --> F["Síntesis por pregunta\nTablas, figuras y conclusión"]
 F --> G["Reporte y actualización\nChecklist y materiales abiertos"]
 C -. "Pilotaje: documentar cambios" .-> B
 E -. "Aclarar criterios" .-> B''' if es else '''flowchart TB
 A["Question and objective\nOutput: RQ and scope"] --> B["Reviewed protocol\nMethods and amendment log"]
 B --> C["Validated search\nQueries, dates and exports"]
 C --> D["Selection\nDecisions and PRISMA flow"]
 D --> E["Critical appraisal and extraction\nJudgements and page-linked data"]
 E --> F["Synthesis by question\nTables, figures and conclusion"]
 F --> G["Reporting and updates\nChecklist and open materials"]
 C -. "Pilot: document amendments" .-> B
 E -. "Clarify criteria" .-> B''')
 mermaid(lang,'review_choice', '''flowchart TB
 A{"¿Cuál es el objetivo?"} -->|Clasificar un campo| B["Mapeo sistemático"]
 A -->|Delimitar conceptos y evidencia| C["Scoping review"]
 A -->|Sintetizar una pregunta concreta| D["Revisión sistemática"]
 A -->|Sintetizar revisiones| E["Revisión terciaria"]
 D --> F{"¿Estimaciones compatibles\ny datos suficientes?"}
 F -->|Sí y justificado| G["Puede incluir metaanálisis"]
 F -->|No| H["Síntesis narrativa, temática\nu otro método explícito"]
 D -.-> I["Añadir fuentes profesionales:\nrevisión multivocal si procede"]''' if es else '''flowchart TB
 A{"What is the objective?"} -->|Classify a field| B["Systematic mapping"]
 A -->|Clarify concepts and evidence| C["Scoping review"]
 A -->|Synthesise a focused question| D["Systematic review"]
 A -->|Synthesise reviews| E["Tertiary review"]
 D --> F{"Compatible estimates\nand sufficient data?"}
 F -->|Yes and justified| G["May include meta-analysis"]
 F -->|No| H["Narrative, thematic\nor other explicit synthesis"]
 D -.-> I["Add practitioner sources:\nmultivocal review where appropriate"]''')
 mermaid(lang,'traceability', '''flowchart TB
 A["RQ1: ¿Qué métricas se emplean\npara evaluar el desempeño?"] --> B["Elegibilidad: residentes o estudiantes;\nsimulador; métrica de desempeño"]
 B --> C["Extracción: estudio, población, métrica,\njustificación y página de origen"]
 C --> D["Análisis: agrupar métricas por función;\ncomparar contextos y limitaciones"]
 D --> E["Figura: población × métrica\nÁrea = número de estudios"]
 E --> F["Respuesta: tiempo, errores y fuerza;\nno se infiere superioridad clínica"]''' if es else '''flowchart TB
 A["RQ1: Which metrics are used\nto assess performance?"] --> B["Eligibility: residents or students;\nsimulator; performance metric"]
 B --> C["Extraction: study, population, metric,\nrationale and source page"]
 C --> D["Analysis: group metrics by function;\ncompare contexts and limitations"]
 D --> E["Figure: population × metric\nArea = number of studies"]
 E --> F["Answer: time, errors and force;\nno clinical superiority inferred"]''')
 mermaid(lang,'search_design', '''flowchart TB
 A["Población\nresident* OR student*"] --> D["Cadena conceptual\nPoblación AND simulador"]
 B["Simulador\nhaptic* OR virtual reality"] --> D
 D --> E["Traducir a campos y sintaxis de cada base\nGuardar cadena exacta, filtros y fecha"]
 E --> F["Comprobar artículos conocidos\nRecuperados / indexados en esa base"]
 F --> G{"¿Faltan artículos relevantes?"}
 G -->|Sí| H["Analizar motivo:\ntérmino, campo, filtro o cobertura"]
 H --> D
 G -->|No en el conjunto de control| I["Ejecutar y exportar\nEl control no prueba exhaustividad"]''' if es else '''flowchart TB
 A["Population\nresident* OR student*"] --> D["Conceptual query\nPopulation AND simulator"]
 B["Simulator\nhaptic* OR virtual reality"] --> D
 D --> E["Translate fields and syntax for each database\nSave exact query, limits and date"]
 E --> F["Check known relevant papers\nRetrieved / indexed in this database"]
 F --> G{"Relevant papers missing?"}
 G -->|Yes| H["Investigate reason:\nterm, field, limit or coverage"]
 H --> D
 G -->|None in the control set| I["Execute and export\nControl does not prove completeness"]''')
 mermaid(lang,'prisma_example', '''flowchart TB
 subgraph DB["Identificación mediante bases de datos"]
 A["Registros: Scopus 24; IEEE Xplore 16\nTotal n = 40"] --> B["Registros cribados\nn = 32"]
 A --> X["Duplicados eliminados\nn = 8"]
 B --> C["Publicaciones buscadas\nn = 10"]
 B --> Y["Registros excluidos\nn = 22"]
 C --> D["Publicaciones evaluadas\nn = 9"]
 C --> Z["No recuperadas\nn = 1"]
 D --> E["Publicaciones incluidas\nn = 5"]
 D --> W["Excluidas: población 2; sin métrica 2\nTotal n = 4"]
 end
 subgraph OT["Identificación mediante otros métodos"]
 O["Búsqueda de citas: publicaciones\nn = 1"] --> P["Buscadas y evaluadas: 1\nNo recuperadas: 0; excluidas: 0"]
 end
 E --> F["Incluidos: 6 estudios; 6 publicaciones\nDATOS FICTICIOS"]
 P --> F''' if es else '''flowchart TB
 subgraph DB["Identification via databases"]
 A["Records: Scopus 24; IEEE Xplore 16\nTotal n = 40"] --> B["Records screened\nn = 32"]
 A --> X["Duplicates removed\nn = 8"]
 B --> C["Reports sought\nn = 10"]
 B --> Y["Records excluded\nn = 22"]
 C --> D["Reports assessed\nn = 9"]
 C --> Z["Reports not retrieved\nn = 1"]
 D --> E["Reports included\nn = 5"]
 D --> W["Excluded: population 2; no metric 2\nTotal n = 4"]
 end
 subgraph OT["Identification via other methods"]
 O["Citation searching: reports\nn = 1"] --> P["Sought and assessed: 1\nNot retrieved: 0; excluded: 0"]
 end
 E --> F["Included: 6 studies; 6 reports\nFICTIONAL DATA"]
 P --> F''')
 mermaid(lang,'snowballing', '''flowchart TB
 A["Semilla S01"] -->|Referencias: atrás| B["Candidato P07\nAplicar elegibilidad"]
 A -->|Citas recibidas: delante| C["Candidato P08\nAplicar elegibilidad"]
 B --> D["Nuevos incluidos\nVincular y deduplicar"]
 C --> D
 D --> E["Siguiente iteración\nRevisar referencias y citas"]
 E --> F{"¿Nuevos elegibles?"}
 F -->|Sí| D
 F -->|No| G["Parar según protocolo\nGuardar fecha, herramienta e iteración"]''' if es else '''flowchart TB
 A["Seed S01"] -->|References: backward| B["Candidate P07\nApply eligibility"]
 A -->|Citing papers: forward| C["Candidate P08\nApply eligibility"]
 B --> D["New included studies\nLink and deduplicate"]
 C --> D
 D --> E["Next iteration\nCheck references and citations"]
 E --> F{"New eligible studies?"}
 F -->|Yes| D
 F -->|No| G["Stop according to protocol\nSave date, tool and iteration"]''')
 mermaid(lang,'records_reports_studies', '''flowchart TB
 R1["Registro R01: Scopus"] --> P1["Publicación P01: congreso"]
 R2["Registro R02: IEEE Xplore"] --> P1
 R3["Registro R03: Scopus"] --> P2["Publicación P02: revista ampliada"]
 P1 --> S["Estudio S01: misma investigación\nDatos complementarios; contar una vez"]
 P2 --> S
 N["3 registros → 2 publicaciones → 1 estudio\nR01 y R02 duplican la misma publicación"]''' if es else '''flowchart TB
 R1["Record R01: Scopus"] --> P1["Report P01: conference paper"]
 R2["Record R02: IEEE Xplore"] --> P1
 R3["Record R03: Scopus"] --> P2["Report P02: extended journal paper"]
 P1 --> S["Study S01: same investigation\nComplementary data; count once"]
 P2 --> S
 N["3 records → 2 reports → 1 study\nR01 and R02 duplicate the same report"]''')
 mermaid(lang,'thematic_synthesis', '''flowchart TB
 A["S01, p. 2: registra tiempo y errores\nS02, p. 2: registra tiempo\nFragmentos ficticios"] --> B["Códigos\nTiempo; errores; fuerza"]
 B --> C["Temas interpretativos\nEficiencia temporal; seguridad de ejecución"]
 C --> D["Conclusión delimitada\nSe registran dimensiones distintas;\nno se demuestra superioridad clínica"]
 E["Comprobar todos los estudios\nS02: datos ausentes no informados\nS04: validez de medida no informada"] -. "Matizar interpretación" .-> D''' if es else '''flowchart TB
 A["S01, p. 2: reports time and errors\nS02, p. 2: reports time\nFictional passages"] --> B["Codes\nTime; errors; force"]
 B --> C["Interpretive themes\nTemporal efficiency; execution safety"]
 C --> D["Bounded conclusion\nDifferent dimensions are recorded;\nclinical superiority is not established"]
 E["Check all studies\nS02: missing data not reported\nS04: measurement validity not reported"] -. "Qualify interpretation" .-> D''')
 mermaid(lang,'human_ai', '''flowchart TB
 A["Protocolo: tarea, modelo, prompt\ny validación independiente"] --> B["IA: ordenar registros\no proponer decisión con evidencia"]
 B --> C["Persona: verificar propuesta\ny consultar documento original"]
 C --> D{"¿Duda o desacuerdo?"}
 D -->|Sí| E["Segunda persona o árbitro\nResolver con criterios explícitos"]
 D -->|No| F["Decisión humana final\nGuardar evidencia y trazabilidad"]
 E --> F
 F --> G["Auditar omisiones y errores\nRevalidar cambios y declarar uso"]''' if es else '''flowchart TB
 A["Protocol: task, model, prompt\nand independent validation"] --> B["AI: rank records\nor propose an evidenced decision"]
 B --> C["Human: verify proposal\nand check original document"]
 C --> D{"Uncertainty or disagreement?"}
 D -->|Yes| E["Second person or arbiter\nResolve using explicit criteria"]
 D -->|No| F["Final human decision\nSave evidence and provenance"]
 E --> F
 F --> G["Audit omissions and errors\nRevalidate changes and disclose use"]''')
# Standard plotting tools; use the downloadable extraction data as source.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
for lang,t in T.items():
 folder=IMG/lang;folder.mkdir(parents=True,exist_ok=True)
 with (OUT/lang/'extraction_example.csv').open(encoding='utf-8-sig') as f:data=list(csv.DictReader(f))
 fig,ax=plt.subplots(figsize=(8,5.3),layout='constrained')
 for x,pop in enumerate(['student','resident']):
  for y,metric in enumerate(['force','errors','time']):
   n=sum(r['population']==t[pop] and t[metric] in r['metrics'].split(';') for r in data)
   if n:ax.scatter(x,y,s=n*620,color='#167c96',alpha=.85,edgecolor='#163247');ax.text(x,y,str(n),ha='center',va='center',color='white',weight='bold',fontsize=15)
 ax.set(xticks=[0,1],xticklabels=[t['student'],t['resident']],yticks=[0,1,2],yticklabels=[t['force'],t['errors'],t['time']],xlim=(-.6,1.6),ylim=(-.55,2.65),xlabel=t['x'],ylabel=t['y'],title=t['title'])
 ax.grid(alpha=.15);ax.set_axisbelow(True)
 fig.text(.5,-.01,t['foot'],ha='center',fontsize=10)
 for ext in ['svg','png']:fig.savefig(folder/f'evidence_map_{lang}.{ext}',dpi=170,bbox_inches='tight')
 plt.close(fig)
 vals=[[0 if r[c]==t['yes'] else 1 for c in ['measurement_validity','missing_data','context']] for r in data]
 fig,ax=plt.subplots(figsize=(8,5),layout='constrained')
 ax.imshow(vals,cmap=ListedColormap(['#d5ece7','#f9e4bc']),vmin=0,vmax=1,aspect='auto')
 ax.set(xticks=[0,1,2],xticklabels=t['domains'],yticks=list(range(6)),yticklabels=[r['study_id'] for r in data],title=t['matrix'])
 for y,row in enumerate(vals):
  for x,v in enumerate(row):ax.text(x,y,('Sí' if lang=='es' else 'Y') if v==0 else ('NI' if lang=='es' else 'NR'),ha='center',va='center',weight='bold',color='#163247')
 fig.text(.5,-.02,t['judgement'],ha='center',fontsize=10)
 for ext in ['svg','png']:fig.savefig(folder/f'appraisal_matrix_{lang}.{ext}',dpi=170,bbox_inches='tight')
 plt.close(fig)
print('Generated 18 editable Graphviz sources, 4 bilingual plots and fictional teaching datasets.')

# Refresh language bundles after regeneration; template files remain editable.
for lang in ('es', 'en'):
    folder = OUT / lang
    with zipfile.ZipFile(folder / 'teaching_materials.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for item in sorted(folder.iterdir()):
            if item.suffix != '.zip':
                archive.write(item, item.name)
