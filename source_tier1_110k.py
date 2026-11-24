import json,os,random,urllib.request as U
R=range
VM=(0,82,337,365,477,1025,0)
VE=(0,94,281,297,512,936,0)
V=(0,100,320,330,500,900,0)
PW=(0,0,1,1,2,4,0)
MT,M,INF=100000,99000,1000000
PS="KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKACEECGKLELMNEKNOELNOEKMNCGKKACEEGIIIILKKIMMMIKMMILLMIKLMIKKKGIIIKKKLJKKKJKKKJKKKJKKKJKKKLMMMKKKKGIIJIKLKILLLKKLLJKLLIKLLIKKKGIIJOQMKOOKKIGGGGEECECCAECCAECCAAEEEEIKKEJOQEKQSEKQSEJOQEIKKAEEEKKKKKKKKKKKKLLLLMMMMPPPPUUUU____KKKK"
PM,PE=[[0]*128 for _ in R(13)],[[0]*128 for _ in R(13)]
for p in R(1,7):
 es=7 if p==1 else 6 if p==6 else p-1
 for r in R(8):
  for f in R(8):
   c=r*4+(f if f<4 else 7-f);s=r*16+f
   m=(ord(PS[(p-1)*32+c])-75)*5+VM[p];e=(ord(PS[es*32+c])-75)*5+VE[p]
   PM[p][s],PE[p][s],PM[-p][s^112],PE[-p][s^112]=m,e,-m,-e
NO=(14,18,31,33,-14,-18,-31,-33)
BD,RD=(15,17,-15,-17),(1,-1,16,-16)
KO=BD+RD
DR=(0,0,NO,BD,RD,KO,KO)
CM={4:12,116:3,7:14,0:13,119:11,112:7}
B64=[0 if s&136 else 1<<((s>>4)*8+(s&7))for s in R(128)]
S88=[(i&7)|((i&56)<<1)for i in R(64)]
_r=random.Random(42).getrandbits
Z=[_r(64)for _ in R(1700)]
u2s=lambda u:ord(u[0])-97+(int(u[1])-1)*16
B=[0]*128;S=1;C=0;E=-1;H=0;K=[0,0];BS=[0,0];OC=[0,0];MG=EG=PH=Y=0;P=[];T=[]
def fen(fn):
 global B,S,C,E,H,BS,OC,MG,EG,PH,Y,P,T
 B=[0]*128;BS=[0,0];OC=[0,0];p=fn.split();r,f=7,0;MG=EG=PH=Y=0
 for c in p[0]:
  if c=="/":r-=1;f=0
  elif c.isdigit():f+=int(c)
  else:
   i="PNBRQKpnbrqk".index(c);q=i+1 if i<6 else 5-i;s=r*16+f;B[s]=q;a=abs(q)
   OC[q<0]|=B64[s]
   if a==6:K[q<0]=s
   elif a==3:BS[q<0]+=1
   MG+=PM[q][s];EG+=PE[q][s];PH+=PW[a];Y^=Z[q*128+s];f+=1
 S=2*(p[1]=="w")-1;C=0
 for c in(p[2]if len(p)>2 else""):
  if c in"KQkq":C|=1<<"KQkq".index(c)
 E=-1 if len(p)<4 or p[3]=="-"else u2s(p[3])
 H=int(p[4])if len(p)>4 and p[4].isdigit()else 0
 Y^=(Z[0]if S<0 else 0)^Z[1+C]^(Z[17+(E&7)]if E>=0 else 0)
 P=[Y];T=[]
def atk(s,w):
 b=B;g=1 if w else-1
 t=s-15*g
 if not(t&136)and b[t]==g:return 1
 t=s-17*g
 if not(t&136)and b[t]==g:return 1
 tg=2*g
 for d in NO:
  t=s+d
  if not(t&136)and b[t]==tg:return 1
 tg=6*g
 for d in KO:
  t=s+d
  if not(t&136)and b[t]==tg:return 1
 t1,t2=3*g,5*g
 for d in BD:
  t=s+d
  while not(t&136):
   p=b[t]
   if p:
    if p==t1 or p==t2:return 1
    break
   t+=d
 t1=4*g
 for d in RD:
  t=s+d
  while not(t&136):
   p=b[t]
   if p:
    if p==t1 or p==t2:return 1
    break
   t+=d
 return 0
def gen(co=0):
 ms=[];ad=ms.append;b=B;u=S;w=u>0;s88=S88;oc=OC[u<0]
 while oc:
  lb=oc&-oc;s=s88[lb.bit_length()-1];oc^=lb
  a=abs(b[s])
  if a==1:
   fw=16*u;t=s+fw
   if not(t&136)and not b[t]:
    if t>>4 in(0,7):
     for pr in((5,2)if co else(5,4,3,2)):ad(s|t<<7|pr<<14)
    elif not co:
     ad(s|t<<7)
     if(s>>4)==(1 if w else 6)and not b[t+fw]:ad(s|(t+fw)<<7)
   for d in(15*u,17*u):
    t=s+d
    if not(t&136):
     if b[t]*u<0:
      if t>>4 in(0,7):
       for pr in((5,2)if co else(5,4,3,2)):ad(s|t<<7|pr<<14)
      else:ad(s|t<<7)
     elif t==E:ad(s|t<<7)
  else:
   for d in DR[a]:
    t=s+d
    while not(t&136):
     p=b[t]
     if p:
      if p*u<0:ad(s|t<<7)
      break
     if not co:ad(s|t<<7)
     if a==2 or a==6:break
     t+=d
   if a==6 and not co:
    r0,fl=(4,1)if w else(116,4)
    if s==r0 and C&(fl*3)and not atk(r0,not w):
     if C&fl and not(b[r0+1]or b[r0+2])and not atk(r0+1,not w)and not atk(r0+2,not w):ad(r0|(r0+2)<<7)
     if C&(fl<<1)and not(b[r0-1]or b[r0-2]or b[r0-3])and not atk(r0-1,not w)and not atk(r0-2,not w):ad(r0|(r0-2)<<7)
 return ms
def mk(m):
 global S,C,E,H,MG,EG,PH,Y
 f,t,pr=m&127,m>>7&127,m>>14&7;b=B;pm=PM;pe=PE;z=Z;q=b[f];u=S;a=abs(q);sd=u<0
 cs=t-16*u if a==1 and t==E else t;cp=b[cs]
 mg,eg,ph,y=MG,EG,PH,Y
 T.append((m,q,cp,C,E,H,BS[0],BS[1],OC[0],OC[1],mg,eg,ph,y))
 b[f]=0;OC[sd]^=B64[f]|B64[t]
 mg-=pm[q][f];eg-=pe[q][f];y^=z[q*128+f]
 if cp:
  b[cs]=0;ac=abs(cp);OC[not sd]^=B64[cs];ph-=PW[ac]
  if ac==3:BS[cp<0]-=1
  mg-=pm[cp][cs];eg-=pe[cp][cs];y^=z[cp*128+cs]
 np=pr*u if pr else q;b[t]=np
 mg+=pm[np][t];eg+=pe[np][t];y^=z[np*128+t]
 if pr:
  ph+=PW[pr]
  if pr==3:BS[sd]+=1
 if a==6:
  K[sd]=t
  if abs(t-f)==2:
   rf,rt=t+1 if t>f else t-2,(f+t)//2;r=b[rf];b[rf]=0;b[rt]=r
   OC[sd]^=B64[rf]|B64[rt];y^=z[r*128+rf]^z[r*128+rt]
   mg+=pm[r][rt]-pm[r][rf];eg+=pe[r][rt]-pe[r][rf]
 if C:
  nc=C&CM.get(f,15)&CM.get(t,15)
  if nc!=C:y^=z[1+C]^z[1+nc];C=nc
 if E>=0:y^=z[17+(E&7)]
 if a==1 and abs(t-f)==32:E=(f+t)//2;y^=z[17+(E&7)]
 else:E=-1
 H=0 if a==1 or cp else H+1;S=-u;y^=z[0]
 MG,EG,PH,Y=mg,eg,ph,y;P.append(y)
def umk():
 global S,C,E,H,MG,EG,PH,Y
 m,q,cp,C,E,H,BS[0],BS[1],OC[0],OC[1],MG,EG,PH,Y=T.pop();P.pop()
 f,t=m&127,m>>7&127;u=-S;b=B;b[f]=q;b[t]=0
 if abs(q)==6:
  K[u<0]=f
  if abs(t-f)==2:rf,rt=t+1 if t>f else t-2,(f+t)//2;b[rf]=b[rt];b[rt]=0
 if cp:b[t-16*u if abs(q)==1 and t==E else t]=cp
 S=u
def ev():p=PH if PH<24 else 24;return((MG*p+EG*(24-p))//24+30*((BS[0]>1)-(BS[1]>1)))*S
TT=[0]*65536;KL=[[0,0]for _ in R(128)];HI=[[0]*128 for _ in R(13)];ND=NL=BM=0
def ng(d,a,b,pl,an=1):
 global ND,S,E,Y,BM
 ND+=1
 if ND>=NL:raise StopIteration
 q=d<=0
 if not q and pl and(H>=100 or P.count(Y)>=2):return 0
 w=S>0;ic=atk(K[not w],not w);tm=0
 if q:
  if not ic:
   sp=ev()
   if sp>=b:return b
   if sp>a:a=sp
   if sp+900<a:return a
 else:
  if ic:d+=1
  ti=Y&65535;e=TT[ti]
  if e and e[0]==Y:
   _,ed,ef,es,tm=e;ad=es-pl if es>M else es+pl if es<-M else es
   if pl and ed>=d and(ef==0 or(ef==1 and ad>=b)or(ef==2 and ad<=a)):return ad
  se=ev()if pl and not ic else 0
  if pl and not ic and an:
   if d<=3 and se-120*d>=b:return b
   if d>=3 and PH>2 and b<M and se>=b:
    oe,ok=E,Y
    if oe>=0:Y^=Z[17+(oe&7)]
    E=-1;S=-S;Y^=Z[0];ns=-ng(d-3-(d>5),-b,-b+1,pl+1,0);S=-S;E,Y=oe,ok
    if ns>=b:return b
 ms=gen(q and not ic)
 if len(ms)>1:
  k1,k2=KL[pl if pl<128 else 127];ba=B;va=V;hi=HI;sc=[]
  for m in ms:
   if m==tm:s=3000000
   else:
    t=m>>7&127;q2=ba[t]
    if m>>14:s=1500000+(m>>14)*100+va[abs(q2)]
    elif q2:s=1000000+10*va[abs(q2)]-va[abs(ba[m&127])]//16
    elif m==k1:s=900000
    elif m==k2:s=800000
    else:s=hi[ba[m&127]][t]
   sc.append((s<<18)|m)
  sc.sort(reverse=1);ms=[x&262143 for x in sc]
 bs,bm,oa,lc=-INF,0,a,0
 fp=not q and pl and d<=2 and not ic and abs(a)<M and se+150*d<=a
 for m in ms:
  f,t=m&127,m>>7&127;pm=B[f];pr=m>>14&7;iq=not B[t]and not pr
  if q and not ic and not pr:
   vc=V[abs(B[t])]if B[t]else 100
   if sp+vc+200<a:continue
   if vc+150<V[abs(pm)]and atk(t,not w):continue
  if fp and iq and lc:continue
  mk(m)
  if atk(K[not w],not w):
   umk();ND+=1
   if ND>=NL:raise StopIteration
   continue
  lc+=1
  if q or lc==1:s=-ng(d-1,-b,-a,pl+1)
  else:
   rd=(2 if lc>=8 else 1)if pl and d>=3 and lc>=4 and iq and not ic else 0
   s=-ng(d-1-rd,-a-1,-a,pl+1)
   if rd and s>a:s=-ng(d-1,-a-1,-a,pl+1)
   if a<s<b:s=-ng(d-1,-b,-a,pl+1)
  umk()
  if s>bs:bs,bm=s,m
  if s>a:a=s
  if a>=b:
   if not q and iq:
    k=KL[pl if pl<128 else 127]
    if m!=k[0]:k[1],k[0]=k[0],m
    HI[pm][t]+=d*d
   break
 if not lc:return-MT+pl if ic else(a if q else 0)
 if q:return a
 if not pl:BM=bm
 e=TT[ti]
 if not e or e[0]!=Y or d>=e[1]:TT[ti]=(Y,d,0 if oa<bs<b else 1 if bs>=b else 2,bs+pl if bs>M else bs-pl if bs<-M else bs,bm)
 return bs
def sel(bg=35000):
 global ND,NL,BM;ND,NL,BM=0,bg,0;bm,d,cs=0,1,0
 while d<=64:
  try:
   al,bt=(cs-50,cs+50)if d>3 else(-INF,INF)
   while 1:
    s=ng(d,al,bt,0)
    if s<=al:al=-INF
    elif s>=bt:bt=INF
    else:break
   bm,cs=BM,s
   if cs>M:break
   d+=1
  except StopIteration:break
 p=bm>>14&7
 return chr(97+(bm&7))+str(1+(bm>>4&7))+chr(97+(bm>>7&7))+str(1+(bm>>11&7))+("  nbrq"[p]if p else"")if bm else None
def main():
 global KL,HI,TT
 url=os.environ["MAKEFUN_ENV_URL"]
 def post(p,d):
  with U.urlopen(U.Request(url+p,json.dumps(d).encode(),{"Content-Type":"application/json"}))as r:return json.load(r)
 while 1:
  try:st=post("/game",{})
  except:break
  if st["status"]=="done":break
  KL=[[0,0]for _ in R(128)];HI=[[0]*128 for _ in R(13)];TT=[0]*65536
  while st["status"]=="your_move":
   fen(st.get("start_fen","rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"))
   for u in st.get("moves",[]):mk(u2s(u[:2])|u2s(u[2:4])<<7|(("  nbrq".index(u[4])<<14)if len(u)>4 else 0))
   l=st.get("legal_moves",[])
   mv=l[0]if len(l)==1 else sel(110000 if PH>12 else 135000 if PH>6 else 160000)
   if l and mv not in l:mv=l[0]
   try:st=post("/move",{"game":st["game"],"move":mv})
   except:break
if __name__=="__main__":main()
