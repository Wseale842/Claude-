"""Fill the PROSYB FCI template (Vaires parts) with the KHAZNA DPGF lines."""
import re, os, shutil, sys, html, openpyxl
W='/tmp/claude-0/-home-user-Claude-/2b0272ac-8e3d-5d40-b9d5-99f068518e86/scratchpad'
SRC=W+'/vaires_x'; DST=W+'/fcigen/khazna_x'
shutil.rmtree(DST,ignore_errors=True); shutil.copytree(SRC,DST)
# ---- data: hours/additions from v5, supplier PRU + source comments from v4
code=open(W+'/work/build_fci_v5.py').read()
_cwd=os.getcwd(); os.chdir(W+'/work'); ns={}; exec(code[:code.index('# existing fourniture')],ns); L=ns['L']; os.chdir(_cwd)
v4=openpyxl.load_workbook(W+'/work/FCI_Khazna_CFA_SSI_AV_IT_v4.xlsx').active
def esc(t): return html.escape(str(t),quote=False)
FAM={23:'VDI-00',5:'VDI-50',6:'VDI-50',7:'VDI-50',8:'VDI-50',9:'VDI-50',10:'VDI-50',11:'VDI-50',12:'VDI-20',13:'VDI-20',14:'DIV-70',15:'DIV-80',
 17:'VDI-00',18:'CFA-95',19:'CFA-70',20:'DIV-80',25:'VDI-00',26:'CFA-95',27:'CFA-70',28:'DIV-80',30:'VDI-20',31:'VDI-00',32:'DIV-80',
 34:'CFA-70',35:'DIV-70',38:'VDI-50',39:'VDI-20',40:'VDI-20',41:'VDI-20',42:'DIV-70',43:'DIV-80',45:'VDI-50',46:'VDI-00',47:'CFA-95',48:'DIV-80',
 52:'SSI-10',53:'SSI-00',54:'SSI-10',55:'SSI-10',56:'SSI-10',58:'SSI-10',59:'SSI-10',60:'DIV-80',62:'SSI-00',64:'DIV-80',66:'SSI-10',67:'SSI-00',69:'DIV-80',
 74:'CFA-30',75:'CFA-30',76:'CFA-30',77:'CFA-40',78:'DIV-80',81:'CVC-60',82:'CVC-60',83:'CVC-60',84:'CVC-60',85:'CVC-60',86:'CVC-60',87:'DIV-70'}
LOT={'VDI':'VDI','AV':'CFA','VID':'CFA','SSI':'SSI','GTB':'CFA'}
CONS={5:('OCTET PLUS / LIEN\'K','BAI4288CN'),6:('OCTET PLUS / LIEN\'K','BAI4288CN'),38:('OCTET PLUS / LIEN\'K','BAI4288CN'),45:('OCTET PLUS / LIEN\'K','BAI4288CN'),
 12:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),13:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),30:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),39:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),40:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),41:('OCTET PLUS / ZVK','ZVKLUZB12OS2'),
 17:('OCTET PLUS / ZVK','ZVKCEFF1212K'),25:('OCTET PLUS / ZVK','ZVKCEFF1212K'),31:('OCTET PLUS / ZVK','ZVKCEFF1212K'),46:('OCTET PLUS / ZVK','ZVKCEFF1212K'),
 19:('SONEPAR','0014640130'),27:('SONEPAR','0014640130'),34:('SONEPAR','0014640130'),26:('UBIQUITI (estimatif)','U6 Pro'),
 54:('AVISS','AE2610CO901'),55:('AVISS','AE2610CO901'),56:('AVISS','AE2610CO901'),58:('AVISS','AE2610CO901'),59:('AVISS','AE2610CO901'),66:('AVISS','AE2610CO901'),
 74:('CCF / HIKVISION','313371'),75:('CCF','313371'),76:('CCF / HIKVISION','313371'),77:('CCF','313371'),81:('WAGO (provisoire)','751-9301'),86:('DELL (provisoire)','')}
CHAP=[('INFORMATIQUE, AUDIOVISUEL & AFFICHAGES — PHASE 2 (2 MOIS)',3,20),('INFORMATIQUE, AUDIOVISUEL & AFFICHAGES — PHASE 3 (5 MOIS)',21,35),
      ('INFORMATIQUE — PHASE 4 (17 MOIS)',36,48),('SÉCURITÉ SSI — PHASE 2 (2 MOIS)',51,60),('SÉCURITÉ SSI — PHASE 3 (5 MOIS)',61,64),
      ('SÉCURITÉ SSI — PHASE 4 (17 MOIS)',65,69),('VIDÉOSURVEILLANCE — PHASE 3 (5 MOIS)',72,78),('GTB / GTE (offre Aetherys attendue — provisoire)',80,87)]
# ---- row builders (styles from template rows)
def blank(r,ab=None):
    c='<c r="A{r}" s="498"/><c r="B{r}" s="457"/>'+''.join('<c r="%s{r}" s="499"/>'%x for x in 'CDEFG')+'<c r="H{r}" s="500"/><c r="I{r}" s="501"/><c r="J{r}" s="481"/><c r="K{r}" s="481"/>'+''.join('<c r="%s{r}" s="482"/>'%x for x in 'LMNOPQ')+'<c r="R{r}" s="481"/><c r="S{r}" s="481"/><c r="T{r}" s="481"/><c r="U{r}" s="483"/><c r="V{r}" s="483"/><c r="W{r}" s="502"/><c r="X{r}" s="558"/><c r="Y{r}" s="485"/><c r="Z{r}" s="486"/><c r="AA{r}" s="486"/>'
    c=c.format(r=r)
    c+=('<c r="AB%d" s="576"><f>SUBTOTAL(9,%s)</f></c>'%(r,ab)) if ab else '<c r="AB%d" s="487"/>'%r
    return '<row r="%d" spans="1:28" s="387" customFormat="1" ht="15">%s</row>'%(r,c)
def title(r,n,t):
    st=['564']*5+['565','566','567','567']+['568']*6+['567']*3+['569','569','570','571','572','573','573','574']
    cols=['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB']
    return '<row r="%d" spans="1:28" s="387" customFormat="1" ht="18" customHeight="1"><c r="A%d" s="577"><v>%d</v></c><c r="B%d" s="563" t="inlineStr"><is><t xml:space="preserve">%s  —  TVA 20 %%</t></is></c>%s</row>'%(r,r,n,r,esc(t),''.join('<c r="%s%d" s="%s"/>'%(c,r,s) for c,s in zip(cols,st)))
def istr(ref,s,t): return '<c r="%s" s="%s" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'%(ref,s,esc(t))
def subhead(r,t):
    return '<row r="%d" spans="1:28" s="386" customFormat="1" ht="16" customHeight="1"><c r="A%d" s="498"/>%s</row>'%(r,r,istr('B%d'%r,'575',t))
def article(r,ref,des,lot,fam,cons,refe,desc,u,q,j,l,n,p):
    def num(c,s,v): return '<c r="%s%d" s="%s"><v>%s</v></c>'%(c,r,s,v) if v not in (None,0,'') else '<c r="%s%d" s="%s"/>'%(c,r,s)
    f=lambda c,s,x:'<c r="%s%d" s="%s"><f>%s</f></c>'%(c,r,s,x.format(r=r))
    ht=max(16,min(110,14.5*((len(des)//62)+1)))
    x=istr('A%d'%r,'498',ref)+istr('B%d'%r,'457',des)+istr('C%d'%r,'458',lot)+istr('D%d'%r,'458',fam)
    x+=(istr('E%d'%r,'458',cons) if cons else '<c r="E%d" s="458"/>'%r)+(istr('F%d'%r,'503',refe) if refe else '<c r="F%d" s="503"/>'%r)+(istr('G%d'%r,'503',desc[:30000]) if desc else '<c r="G%d" s="503"/>'%r)
    x+=istr('H%d'%r,'448',u)+num('I','451',q)+num('J','444',round(j,2))+f('K','504','J{r}*$I{r}')+num('L','445',l)+f('M','505','L{r}*$I{r}')+num('N','506',n)+f('O','505','N{r}*$I{r}')+num('P','507',p)+f('Q','505','P{r}*$I{r}')
    x+=f('R','561','$L{r}*$M$14+$N{r}*$O$14+$P{r}*$Q$14')+f('S','504','R{r}*$I{r}')+f('T','504','$S{r}+$K{r}')+f('U','483','HLOOKUP($C{r},Recap_FCI!$K$9:$S$20,11,FALSE)')+f('V','483','HLOOKUP($C{r},Recap_FCI!$K$9:$S$20,12,FALSE)')
    x+=f('W','502','$J{r}*$U{r}')+f('X','560','$R{r}*$V{r}')+f('Y','485','X{r}+W{r}')+f('Z','486','$W{r}*$I{r}')+f('AA','486','$X{r}*$I{r}')+f('AB','508','$Y{r}*$I{r}')
    return '<row r="%d" spans="1:28" s="386" customFormat="1" ht="%.1f" customHeight="1">%s</row>'%(r,ht,x)
# ---- build DPGF rows
rows=[]; r=19; art_ranges=[]; agg={}; famagg={}
for n,(t,a,b) in enumerate(CHAP,1):
    rows.append(title(r,n,t)); r+=1; first=r; k=0
    for dr in range(a,b+1):
        A=v4.cell(dr,1).value; B=v4.cell(dr,2).value; U=v4.cell(dr,3).value; Q=v4.cell(dr,4).value
        if B is None: continue
        if U is None and Q is None:
            if str(A).startswith('4') or str(A) in ('5','6','7') or str(A).startswith(('5.','6.')): continue
            rows.append(subhead(r,('HORS LOT — ' if A=='Hors lot' else '')+B)); r+=1; continue
        if A=='LOT GC':
            rows.append(subhead(r,'HORS LOT (lot GC) — '+B)); r+=1; continue
        dom,add,h,hyp=L[dr] if dr in L else (L[dr+2][0],0,{},''); k+=1
        pru=(v4.cell(dr,5).value or 0)+add
        src=v4.cell(dr,7).value or ''
        cons,refe=CONS.get(dr,('',''))
        lot=LOT[dom]; nh=h.get('Tech',0)+h.get('SSI',0)
        desc=('MO : '+hyp+' | ' if hyp else '')+src+(' | Heures technicien SSI comptées au taux technicien Cfa.' if h.get('SSI') else '')
        rows.append(article(r,'%d.%d'%(n,k),B,lot,FAM[dr],cons,refe,desc,'ens' if U=='Ens' else 'u',Q,pru,h.get('Mont',0),nh,h.get('BE',0)))
        agg.setdefault(lot,[0,0,0,0]); a_=agg[lot]; a_[0]+=pru*Q; a_[1]+=h.get('Mont',0)*Q; a_[2]+=nh*Q; a_[3]+=h.get('BE',0)*Q
        famagg[(FAM[dr],lot)]=famagg.get((FAM[dr],lot),0)+pru*Q
        art_ranges.append(r); r+=1
    last=r-1; rows.append(blank(r)); r+=1
    rows.append(blank(r,'AB%d:AB%d'%(first,last))); r+=1
cost=r
rows.append('<row r="%d" spans="1:28" s="393" customFormat="1" ht="17"><c r="A%d" s="509"/><c r="B%d" s="510"/><c r="C%d" s="511"/><c r="D%d" s="512"/><c r="E%d" s="512"/><c r="F%d" s="512"/><c r="G%d" s="578"/><c r="H%d" s="579"/><c r="I%d" s="580"/><c r="J%d" s="581"/><c r="K%d" s="513"><f>SUBTOTAL(9,K18:K%d)</f></c><c r="L%d" s="514"/><c r="M%d" s="514"><f>SUBTOTAL(9,M18:M%d)</f></c><c r="N%d" s="514"/><c r="O%d" s="514"><f>SUBTOTAL(9,O18:O%d)</f></c><c r="P%d" s="514"/><c r="Q%d" s="514"><f>SUBTOTAL(9,Q18:Q%d)</f></c><c r="R%d" s="513"/><c r="S%d" s="513"><f>SUBTOTAL(9,S18:S%d)</f></c><c r="T%d" s="513"><f>SUBTOTAL(9,T18:T%d)</f></c><c r="U%d" s="515"/><c r="V%d" s="639"/><c r="W%d" s="638"/><c r="X%d" s="516"/><c r="Y%d" s="517"/><c r="Z%d" s="518"/><c r="AA%d" s="519"/><c r="AB%d" s="520"/></row>'.replace('%d','{0}').replace('{0}',str(cost),1) if False else None)
rows.pop()
def costrow(r):
    c=[('A','509'),('B','510'),('C','511'),('D','512'),('E','512'),('F','512'),('G','578'),('H','579'),('I','580'),('J','581')]
    x=''.join('<c r="%s%d" s="%s"/>'%(a,r,s) for a,s in c)
    for col,s,fm in [('K','513',1),('L','514',0),('M','514',1),('N','514',0),('O','514',1),('P','514',0),('Q','514',1),('R','513',0),('S','513',1),('T','513',1)]:
        x+=('<c r="%s%d" s="%s"><f>SUBTOTAL(9,%s18:%s%d)</f></c>'%(col,r,s,col,col,r-1)) if fm else '<c r="%s%d" s="%s"/>'%(col,r,s)
    x+=''.join('<c r="%s%d" s="%s"/>'%(a,r,s) for a,s in [('U','515'),('V','639'),('W','638'),('X','516'),('Y','517'),('Z','518'),('AA','519'),('AB','520')])
    return '<row r="%d" spans="1:28" s="393" customFormat="1" ht="17">%s</row>'%(r,x)
cols=['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
def totrow(r,label,s1,s2,s3,tail):
    return '<row r="%d" spans="1:28" s="392" customFormat="1" ht="17">%s%s<c r="Y%d" s="%s"/>%s</row>'%(r,istr('A%d'%r,s1,label),''.join('<c r="%s%d" s="%s"/>'%(c,r,s2) for c in cols),r,s3,tail)
rows.append(costrow(cost)); ht=cost+1
rows.append(totrow(ht,'TOTAL GÉNÉRAL HORS TAXES','711','712','713','<c r="Z{0}" s="518"><f>SUBTOTAL(9,Z18:Z{1})</f></c><c r="AA{0}" s="519"><f>SUBTOTAL(9,AA18:AA{1})</f></c><c r="AB{0}" s="520"><f>SUBTOTAL(9,AB18:AB{1})</f></c>'.format(ht,ht-1)))
rows.append(totrow(ht+1,'TVA 20 %','714','715','715','<c r="Z{0}" s="521"/><c r="AA{0}" s="521"/><c r="AB{0}" s="635"><f>AB{1}*0.2</f></c>'.format(ht+1,ht)))
rows.append(totrow(ht+2,'TOTAL GÉNÉRAL TTC','716','717','718','<c r="Z{0}" s="522"/><c r="AA{0}" s="523"/><c r="AB{0}" s="524"><f>AB{1}+AB{2}</f></c>'.format(ht+2,ht,ht+1)))
nota=ht+3
NOTA=("Nota : Offre établie sur la DPGF FR02201-ENG-ELEC-OTH-1029 (lots 4 à 7), hors lot GC et hors centrales SSI des îlots. "
 "Exploitation ≈ 26 mois, phases 2, 3 et 4. Fournitures selon devis Sonepar 0014640130, Octet Plus DE044128 (hors coffrets IP55 fournis par SPIE), CCF 313371, AVISS AE2610CO901 ; "
 "lignes « estimatif » à confirmer (supports et totems afficheurs, Rally Mic Pod, serveur de diffusion, câbles CR1-C1, mâts caméras, bornes Wi-Fi) ; lot GTB provisoire dans l'attente de l'offre Aetherys. "
 "Switchs informatiques fournis par EXYTE. Main-d'œuvre en hypothèse optimiste. Non compris : études d'exécution EXE.CFA (§2), maintenance 29 mois (§8), nacelle.")
rows.append('<row r="%d" spans="1:28" ht="75" customHeight="1"><c r="A%d" s="388"/>%s</row>'%(nota,nota,istr('B%d'%nota,'395',NOTA)))
for e in range(nota+1,nota+24): rows.append('<row r="%d" spans="1:28"/>'%e)
end=nota+23
s=open(DST+'/xl/worksheets/sheet4.xml',encoding='utf-8').read()
i=s.index('<sheetData>')+len('<sheetData>'); j=s.index('</sheetData>')
data=s[i:j]
keep=[m.group(0) for m in re.finditer(r'<row [^>]*?(?:/>|>.*?</row>)',data,re.S) if int(re.search(r'r="(\d+)"',m.group(0)).group(1))<=18]
OBJ='OBJET : KHAZNA ORY01 — Fouju (77) — Installations provisoires base vie & chantier — Lot courants faibles : informatique, audiovisuel, affichage, SSI, vidéosurveillance, GTB (DPGF lots 4 à 7)'
keep=[re.sub(r'(<c r="B17" s="575" t="inlineStr"><is><t xml:space="preserve">).*?(</t>)',lambda m:m.group(1)+esc(OBJ)+m.group(2),k,flags=re.S) for k in keep]
s=s[:i]+''.join(keep)+''.join(rows)+s[j:]
s=re.sub(r'<dimension ref="[^"]*"/>','<dimension ref="A1:AB%d"/>'%end,s)
s=re.sub(r'<mergeCell ref="A\d+:Y\d+"/>','',s)
s=re.sub(r'<mergeCells count="\d+">',lambda m:'<mergeCells count="8">',s)
s=s.replace('</mergeCells>','<mergeCell ref="A%d:Y%d"/><mergeCell ref="A%d:Y%d"/><mergeCell ref="A%d:Y%d"/></mergeCells>'%(ht,ht,ht+1,ht+1,ht+2,ht+2))
s=re.sub(r'<conditionalFormatting sqref="C19:C\d+">','<conditionalFormatting sqref="C19:C%d">'%(ht-1),s)
def sq(col):
    out=[];st=pr=None
    for x in art_ranges:
        if st is None: st=pr=x
        elif x==pr+1: pr=x
        else: out.append('%s%d:%s%d'%(col,st,col,pr)); st=pr=x
    out.append('%s%d:%s%d'%(col,st,col,pr)); return ' '.join(out)
s=re.sub(r'(<dataValidation [^>]*?sqref=")C[^"]*(")',lambda m:m.group(1)+sq('C')+m.group(2),s,count=1)
s=re.sub(r'(<dataValidation [^>]*?sqref=")D[^"]*(")',lambda m:m.group(1)+sq('D')+m.group(2),s,count=1)
s=re.sub(r'<brk id="\d+"','<brk id="%d"'%(nota+1),s)
open(DST+'/xl/worksheets/sheet4.xml','w',encoding='utf-8').write(s)
# footer shapes of DPGF (drawing2) anchored rows 59-72 -> move under Nota
d=open(DST+'/xl/drawings/drawing2.xml',encoding='utf-8').read()
shift=(nota+9)-59
def mv(m):
    v=int(m.group(2)); return m.group(1)+str(v+shift if v>=50 else v)+m.group(3)
d=re.sub(r'(<xdr:row>)(\d+)(</xdr:row>)',mv,d)
CART=['Client : EXYTE — entreprise générale','Adresse : RD 57 — 77390 Fouju','Tel : ','Mail : ','Affaire : KHAZNA ORY01 — Base vie & chantier — Courants faibles','References : [ N° d\'offre ]','Version : 1','Date : 16/10/2026']
# replace texts of the rounded rectangle (client card): keep runs order, map by prefix
for pre,new in [('Client',CART[0]),('Adresse',CART[1]),('Affaire',CART[4]),('Date',CART[7])]:
    d=re.sub(r'(<a:t>)%s[^<]*(</a:t>)'%pre,lambda m:m.group(1)+esc(new)+m.group(2),d,count=1)
open(DST+'/xl/drawings/drawing2.xml','w',encoding='utf-8').write(d)
# page de garde (drawing1)
p=open(DST+'/xl/drawings/drawing1.xml',encoding='utf-8').read()
PG={'pg_affaire':'KHAZNA ORY01 — Courants faibles base vie & chantier','pg_client':'EXYTE — entreprise générale','pg_ref':"[ N° d'offre ]",
    'pg_site':'RD 57 — 77390 Fouju (77)','pg_lot':'VDI / CFA / SSI / GTB','pg_date':'16/10/2026','pg_resp':'Woody SEALE'}
for nm,val in PG.items():
    m=re.search(r'name="%s".*?</xdr:sp>'%nm,p,re.S)
    if not m: print('shape?',nm); continue
    blk=m.group(0); ts=re.findall(r'<a:t>[^<]*</a:t>',blk)
    nb=blk.replace(ts[0],'<a:t>%s</a:t>'%esc(val),1)
    for t in ts[1:]: nb=nb.replace(t,'<a:t></a:t>',1)
    p=p.replace(blk,nb)
open(DST+'/xl/drawings/drawing1.xml','w',encoding='utf-8').write(p)
# workbook print area
wbx=open(DST+'/xl/workbook.xml',encoding='utf-8').read()
wbx=wbx.replace('DPGF!$A$1:$AB$73','DPGF!$A$1:$AB$%d'%end)
open(DST+'/xl/workbook.xml','w',encoding='utf-8').write(wbx)
# ---- Recap
R=open(DST+'/xl/worksheets/sheet2.xml',encoding='utf-8').read()
def setc(ref,val,kind='n'):
    global R
    m=re.search(r'<c r="%s"( s="\d+")?[^>]*?(/>|>.*?</c>)'%ref,R,re.S)
    st=m.group(1) or ''
    if val is None: new='<c r="%s"%s/>'%(ref,st)
    elif kind=='s': new='<c r="%s"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'%(ref,st,esc(val))
    elif kind=='f': new='<c r="%s"%s><f>%s</f></c>'%(ref,st,val)
    else: new='<c r="%s"%s><v>%s</v></c>'%(ref,st,round(val,2))
    R=R[:m.start()]+new+R[m.end():]
setc('C2','EXYTE','s'); setc('C3','KHAZNA ORY01 — Base vie & chantier — Lot courants faibles','s'); setc('C4','RD 57 — 77390 Fouju (77)','s')
setc('C6','VDI / CFA / SSI / GTB','s'); setc('G2',"[ N° d'offre ]",'s'); setc('G13','DPGF!AB%d'%ht,'f')
LC={'VDI':'K','CFO':'L','CFA':'M','SSI':'N','CVC':'O','OC':'P'}
for lot,c in LC.items():
    a_=agg.get(lot,[0,0,0,0])
    setc(c+'31',a_[0] or None); setc(c+'43',a_[1] or None); setc(c+'46',a_[2] or None); setc(c+'49',a_[3] or None)
FAMLAB={}
for rr in openpyxl.load_workbook(W+'/fcigen/vaires_test.xlsx')['FAMILLE'].iter_rows(min_row=2,values_only=True):
    if rr[0]: FAMLAB[rr[0]]=rr[1]
fams={}
for (fm,lot),v in famagg.items(): fams.setdefault(fm,{})[lot]=fams.get(fm,{}).get(lot,0)+v
items=sorted(fams.items(),key=lambda kv:-sum(kv[1].values()))
if len(items)>10:
    rest={}; 
    for fm,d_ in items[9:]:
        for lot,v in d_.items(): rest[lot]=rest.get(lot,0)+v
    items=items[:9]+[('AUTRES',rest)]
for k_ in range(10):
    row=32+k_
    if k_<len(items):
        fm,d_=items[k_]
        setc('B%d'%row,'%s : %s'%(fm,FAMLAB.get(fm,'familles diverses')) if fm!='AUTRES' else 'Autres familles','s'); setc('F%d'%row,'SUM($K%d:$P%d)'%(row,row),'f')
        for lot,c in LC.items(): setc('%s%d'%(c,row),d_.get(lot) or None)
    else:
        setc('B%d'%row,None); setc('F%d'%row,None)
        for c in LC.values(): setc('%s%d'%(c,row),None)
for prof,row in (('Monteur',43),('Tech',46),('RT',49)):
    m=re.search(r'<c r="B%d"( s="\d+")?'%row,R)
    setc('B%d'%row,'X','s')
open(DST+'/xl/worksheets/sheet2.xml','w',encoding='utf-8').write(R)
print('rows end',end,'HT row',ht,'articles',len(art_ranges))
print({k:[round(x,2) for x in v] for k,v in agg.items()})
