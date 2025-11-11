import http.server
import socketserver

PORT = 8000

HTML = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Grafo de 7 estados — México (Leaflet)</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Leaflet -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  :root { --bg:#0f172a; --card:#111827; --muted:#94a3b8; --accent:#38bdf8; }
  html, body { height:100%; margin:0; font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif; background:#0b1020; color:#e5e7eb;}
  .app { display:grid; grid-template-columns: 340px 1fr 420px; grid-template-rows: 100vh; gap:10px; padding:10px; box-sizing:border-box;}
  .panel, .side { background:#0f172a; border:1px solid #1f2937; border-radius:14px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,.25);}
  .panel h2, .side h2 { margin:0; padding:12px 14px; font-size:16px; background:#111827; border-bottom:1px solid #1f2937;}
  .controls { padding:12px; display:flex; flex-direction:column; gap:10px; }
  select { width:100%; height:52vh; background:#0b1222; color:#e5e7eb; border:1px solid #374151; border-radius:10px; padding:8px;}
  button { background:#22c55e; color:#04111f; border:none; padding:10px 12px; border-radius:10px; font-weight:700; cursor:pointer;}
  button.secondary{ background:#334155; color:#e5e7eb;}
  #map { width:100%; height:100%; }
  .side .content { padding:12px; height:calc(100% - 48px); overflow:auto; }
  .badge { display:inline-block; padding:2px 8px; background:#1f2937; border-radius:999px; font-size:12px; color:#cbd5e1; }
  .kpi { font-weight:800; color:#22c55e; }
  .muted { color:#94a3b8; }
  .mono { font-family: ui-monospace, Menlo, Monaco, Consolas, monospace;}
  hr { border:none; border-top:1px solid #1f2937; margin:12px 0;}
</style>
</head>
<body>
<div class="app">
  <div class="panel">
    <h2>Selecciona 7 estados</h2>
    <div class="controls">
      <select id="lst" multiple></select>
      <div style="display:flex; gap:8px;">
        <button id="btnRun">Usar selección (7)</button>
        <button id="btnClear" class="secondary">Limpiar</button>
      </div>
      <div class="muted">Ctrl/⌘ + clic para seleccionar múltiples.</div>
    </div>
  </div>

  <div class="panel">
    <h2>Mapa (México)</h2>
    <div id="map"></div>
  </div>

  <div class="side">
    <h2>Resultados</h2>
    <div class="content mono" id="out"></div>
  </div>
</div>

<script>
/* ================== Datos ================== */
const CENTROIDES = {
  "Aguascalientes":[21.8853,-102.2916],"Baja California":[30.8406,-115.2838],
  "Baja California Sur":[26.0444,-111.6661],"Campeche":[19.1640,-90.4519],
  "Coahuila":[27.0587,-101.7068],"Colima":[19.1223,-104.0070],
  "Chiapas":[16.7569,-93.1292],"Chihuahua":[28.6329,-106.0691],
  "Ciudad de México":[19.4326,-99.1332],"Durango":[24.5593,-104.6588],
  "Guanajuato":[21.0190,-101.2574],"Guerrero":[17.4392,-99.5451],
  "Hidalgo":[20.4799,-98.9636],"Jalisco":[20.6595,-103.3494],
  "México":[19.2920,-99.6569],"Michoacán":[19.5665,-101.7068],
  "Morelos":[18.6813,-99.1013],"Nayarit":[21.7514,-104.8455],
  "Nuevo León":[25.5922,-99.9962],"Oaxaca":[17.0594,-96.7216],
  "Puebla":[19.0414,-98.2063],"Querétaro":[20.5888,-100.3899],
  "Quintana Roo":[19.1817,-88.4791],"San Luis Potosí":[22.1565,-100.9855],
  "Sinaloa":[24.8091,-107.3940],"Sonora":[29.2972,-110.3309],
  "Tabasco":[17.8409,-92.6189],"Tamaulipas":[24.2669,-98.8363],
  "Tlaxcala":[19.3182,-98.2375],"Veracruz":[19.1738,-96.1342],
  "Yucatán":[20.7099,-89.0943],"Zacatecas":[22.7709,-102.5833]
};

/* ================== UI ================== */
const lst=document.getElementById("lst");
Object.keys(CENTROIDES).sort().forEach(n=>{
  const o=document.createElement("option");o.value=o.textContent=n;lst.appendChild(o);
});
document.getElementById("btnClear").onclick=()=>[...lst.options].forEach(o=>o.selected=false);

/* ================== Mapa ================== */
const map=L.map("map").setView([23.7,-102.5],5);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",{maxZoom:19}).addTo(map);
const layerEdges=L.layerGroup().addTo(map);
const layerMarkers=L.layerGroup().addTo(map);

function hav(lat1,lon1,lat2,lon2){
  const R=6371,p1=lat1*Math.PI/180,p2=lat2*Math.PI/180;
  const dphi=(lat2-lat1)*Math.PI/180,dl=(lon2-lon1)*Math.PI/180;
  const a=Math.sin(dphi/2)**2 + Math.cos(p1)*Math.cos(p2)*Math.sin(dl/2)**2;
  return 2*R*Math.asin(Math.sqrt(a));
}
function perm(arr){
  if(arr.length<=1) return [arr.slice()];
  let r=[];
  for(let i=0;i<arr.length;i++){
    let rest=[...arr.slice(0,i),...arr.slice(i+1)];
    for(let p of perm(rest)) r.push([arr[i],...p]);
  }
  return r;
}

document.getElementById("btnRun").onclick=()=>{
  const sel=[...lst.selectedOptions].map(o=>o.value);
  if(sel.length!==7){alert("Selecciona exactamente 7.");return;}

  layerEdges.clearLayers();layerMarkers.clearLayers();
  const coords={};

  sel.forEach(n=>{
    coords[n]=CENTROIDES[n];
    let [lat,lon]=coords[n];
    L.circleMarker([lat,lon],{radius:7,color:"#3e2723",fillColor:"#ff6f00",fillOpacity:1,weight:2})
      .addTo(layerMarkers)
      .bindTooltip(n,{permanent:true,offset:[10,-10]});
  });

  for(let i=0;i<7;i++){
    for(let j=i+1;j<7;j++){
      let a=sel[i],b=sel[j];
      let [la,lo]=coords[a],[lb,lo2]=coords[b];
      let km=Math.round(hav(la,lo,lb,lo2));
      L.polyline([[la,lo],[lb,lo2]],{color:"#777"}).addTo(layerEdges);
      L.marker([(la+lb)/2,(lo+lo2)/2],{opacity:0})
        .addTo(layerEdges).bindTooltip(String(km),{permanent:true});
    }
  }

  let start=sel[0], others=sel.slice(1);
  let best=null, bc=1e12;
  for(let p of perm(others)){
    let path=[start,...p], cost=0;
    for(let i=0;i<path.length-1;i++){
      let a=coords[path[i]],b=coords[path[i+1]];
      cost+=hav(...a,...b);
    }
    if(cost<bc){bc=cost;best=path;}
  }
  let costA=Math.round(bc);
  let cycle=[...best,best[0]];
  let last=Math.round(hav(...coords[best.at(-1)],...coords[best[0]]));
  let costB=costA+last;

  for(let i=0;i<best.length-1;i++){
    L.polyline([coords[best[i]],coords[best[i+1]]],{color:"#d32f2f",weight:5}).addTo(layerEdges);
  }
  L.polyline([coords[best.at(-1)],coords[best[0]]],{color:"#22c55e",weight:5,dashArray:"8 6"}).addTo(layerEdges);

  const out=document.getElementById("out");
  out.innerHTML = 
    sel.map((n,i)=>`${i+1}. ${n}`).join("<br>")+
    `<hr>(a) ${best.join(" → ")}<br>Costo: ${costA} km<br><br>(b) ${cycle.join(" → ")}<br>Costo: ${costB} km<hr>`;
};
</script>
</body>
</html>
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML.encode("utf-8"))
        else:
            self.send_error(404, "Archivo no encontrado")


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\nServidor activo en:\n👉 http://localhost:{PORT}\n")
    httpd.serve_forever()

