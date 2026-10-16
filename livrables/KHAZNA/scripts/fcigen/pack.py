"""Rebuild a valid .xlsx from the partially mirrored Vaires FCI parts (no .rels/.vml/.bin available)."""
import os, re, sys, zipfile, shutil
SRC, OUT = sys.argv[1], sys.argv[2]
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PR='http://schemas.openxmlformats.org/package/2006/relationships'
def rels(items):
    x='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="%s">'%PR
    for rid,typ,tgt in items: x+='<Relationship Id="%s" Type="%s/%s" Target="%s"/>'%(rid,REL if not typ.startswith('http') else '',typ,tgt) if not typ.startswith('http') else '<Relationship Id="%s" Type="%s" Target="%s"/>'%(rid,typ,tgt)
    return x+'</Relationships>'
files={}
for root,_,fs in os.walk(SRC):
    for f in fs:
        p=os.path.relpath(os.path.join(root,f),SRC).replace(os.sep,'/')
        files[p]=open(os.path.join(root,f),'rb').read()
# drop parts we cannot reference correctly
for p in list(files):
    if p.startswith(('customUI/','customXml/')) or p in ('xl/comments1.xml','xl/comments2.xml','xl/externalLinks/externalLink1.xml'):
        del files[p]
ct=files['[Content_Types].xml'].decode()
ct=ct.replace('application/vnd.ms-excel.sheet.macroEnabled.main+xml','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml')
ct=re.sub(r'<Override PartName="/(customUI|customXml)/[^"]*"[^>]*/>','',ct)
ct=re.sub(r'<Override PartName="/xl/(vbaProject\.bin|comments\d\.xml|externalLinks/externalLink1\.xml)"[^>]*/>','',ct)
ct=ct.replace('ContentType="image/.jpg"','ContentType="image/jpeg"')
files['[Content_Types].xml']=ct.encode()
wb=files['xl/workbook.xml'].decode()
wb=re.sub(r'<externalReferences>.*?</externalReferences>','',wb)
wb=re.sub(r'<definedName name="intrusions?">[^<]*</definedName>','',wb)
files['xl/workbook.xml']=wb.encode()
files['_rels/.rels']=rels([('rId1','officeDocument','xl/workbook.xml'),
 ('rId2','http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties','docProps/core.xml'),
 ('rId3','extended-properties','docProps/app.xml'),('rId4','custom-properties','docProps/custom.xml')]).encode()
wr=[('rId%d'%i,'worksheet','worksheets/sheet%d.xml'%i) for i in range(1,9)]
wr+=[('rId20','theme','theme/theme1.xml'),('rId21','styles','styles.xml'),('rId22','sharedStrings','sharedStrings.xml')]
files['xl/_rels/workbook.xml.rels']=rels(wr).encode()
# sheets: strip printer/legacy refs, wire drawings
dmap={1:'drawing1',4:'drawing2',5:'drawing3',8:'drawing4'}
for i in range(1,9):
    p='xl/worksheets/sheet%d.xml'%i; s=files[p].decode()
    s=re.sub(r'(<pageSetup[^>]*?) r:id="rId\d+"',r'\1',s)
    s=re.sub(r'<legacyDrawing(HF)? r:id="rId\d+"/>','',s)
    s=re.sub(r'<drawing r:id="rId\d+"/>','<drawing r:id="rIdD"/>',s)
    files[p]=s.encode()
    if i in dmap: files['xl/worksheets/_rels/sheet%d.xml.rels'%i]=rels([('rIdD','drawing','../drawings/%s.xml'%dmap[i])]).encode()
img={'drawing1':{'rId1':'image1.png'},'drawing2':{'rId1':'image2.png','rId2':'image3.png'},
     'drawing3':{'rId1':'image5.png','rId2':'image7.png','rId3':'image6.png'},'drawing4':{'rId1':'image2.png'}}
for d,m in img.items():
    files['xl/drawings/_rels/%s.xml.rels'%d]=rels([(k,'image','../media/'+v) for k,v in m.items()]).encode()
order=['[Content_Types].xml','_rels/.rels']+sorted(p for p in files if p not in ('[Content_Types].xml','_rels/.rels'))
with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
    for p in order: z.writestr(p,files[p])
print('ok',OUT,len(files))
