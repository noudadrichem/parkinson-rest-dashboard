(function(e){function t(t){for(var s,r,l=t[0],c=t[1],o=t[2],u=0,f=[];u<l.length;u++)r=l[u],n[r]&&f.push(n[r][0]),n[r]=0;for(s in c)Object.prototype.hasOwnProperty.call(c,s)&&(e[s]=c[s]);d&&d(t);while(f.length)f.shift()();return i.push.apply(i,o||[]),a()}function a(){for(var e,t=0;t<i.length;t++){for(var a=i[t],s=!0,l=1;l<a.length;l++){var c=a[l];0!==n[c]&&(s=!1)}s&&(i.splice(t--,1),e=r(r.s=a[0]))}return e}var s={},n={app:0},i=[];function r(t){if(s[t])return s[t].exports;var a=s[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=e,r.c=s,r.d=function(e,t,a){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},r.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)r.d(a,s,function(t){return e[t]}.bind(null,s));return a},r.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],c=l.push.bind(l);l.push=t,l=l.slice();for(var o=0;o<l.length;o++)t(l[o]);var d=c;i.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("56d7")},4678:function(e,t,a){var s={"./af":"2bfb","./af.js":"2bfb","./ar":"8e73","./ar-dz":"a356","./ar-dz.js":"a356","./ar-kw":"423e","./ar-kw.js":"423e","./ar-ly":"1cfd","./ar-ly.js":"1cfd","./ar-ma":"0a84","./ar-ma.js":"0a84","./ar-sa":"8230","./ar-sa.js":"8230","./ar-tn":"6d83","./ar-tn.js":"6d83","./ar.js":"8e73","./az":"485c","./az.js":"485c","./be":"1fc1","./be.js":"1fc1","./bg":"84aa","./bg.js":"84aa","./bm":"a7fa","./bm.js":"a7fa","./bn":"9043","./bn.js":"9043","./bo":"d26a","./bo.js":"d26a","./br":"6887","./br.js":"6887","./bs":"2554","./bs.js":"2554","./ca":"d716","./ca.js":"d716","./cs":"3c0d","./cs.js":"3c0d","./cv":"03ec","./cv.js":"03ec","./cy":"9797","./cy.js":"9797","./da":"0f14","./da.js":"0f14","./de":"b469","./de-at":"b3eb","./de-at.js":"b3eb","./de-ch":"bb71","./de-ch.js":"bb71","./de.js":"b469","./dv":"598a","./dv.js":"598a","./el":"8d47","./el.js":"8d47","./en-SG":"cdab","./en-SG.js":"cdab","./en-au":"0e6b","./en-au.js":"0e6b","./en-ca":"3886","./en-ca.js":"3886","./en-gb":"39a6","./en-gb.js":"39a6","./en-ie":"e1d3","./en-ie.js":"e1d3","./en-il":"7333","./en-il.js":"7333","./en-nz":"6f50","./en-nz.js":"6f50","./eo":"65db","./eo.js":"65db","./es":"898b","./es-do":"0a3c","./es-do.js":"0a3c","./es-us":"55c9","./es-us.js":"55c9","./es.js":"898b","./et":"ec18","./et.js":"ec18","./eu":"0ff2","./eu.js":"0ff2","./fa":"8df4","./fa.js":"8df4","./fi":"81e9","./fi.js":"81e9","./fo":"0721","./fo.js":"0721","./fr":"9f26","./fr-ca":"d9f8","./fr-ca.js":"d9f8","./fr-ch":"0e49","./fr-ch.js":"0e49","./fr.js":"9f26","./fy":"7118","./fy.js":"7118","./ga":"5120","./ga.js":"5120","./gd":"f6b4","./gd.js":"f6b4","./gl":"8840","./gl.js":"8840","./gom-latn":"0caa","./gom-latn.js":"0caa","./gu":"e0c5","./gu.js":"e0c5","./he":"c7aa","./he.js":"c7aa","./hi":"dc4d","./hi.js":"dc4d","./hr":"4ba9","./hr.js":"4ba9","./hu":"5b14","./hu.js":"5b14","./hy-am":"d6b6","./hy-am.js":"d6b6","./id":"5038","./id.js":"5038","./is":"0558","./is.js":"0558","./it":"6e98","./it-ch":"6f12","./it-ch.js":"6f12","./it.js":"6e98","./ja":"079e","./ja.js":"079e","./jv":"b540","./jv.js":"b540","./ka":"201b","./ka.js":"201b","./kk":"6d79","./kk.js":"6d79","./km":"e81d","./km.js":"e81d","./kn":"3e92","./kn.js":"3e92","./ko":"22f8","./ko.js":"22f8","./ku":"2421","./ku.js":"2421","./ky":"9609","./ky.js":"9609","./lb":"440c","./lb.js":"440c","./lo":"b29d","./lo.js":"b29d","./lt":"26f9","./lt.js":"26f9","./lv":"b97c","./lv.js":"b97c","./me":"293c","./me.js":"293c","./mi":"688b","./mi.js":"688b","./mk":"6909","./mk.js":"6909","./ml":"02fb","./ml.js":"02fb","./mn":"958b","./mn.js":"958b","./mr":"39bd","./mr.js":"39bd","./ms":"ebe4","./ms-my":"6403","./ms-my.js":"6403","./ms.js":"ebe4","./mt":"1b45","./mt.js":"1b45","./my":"8689","./my.js":"8689","./nb":"6ce3","./nb.js":"6ce3","./ne":"3a39","./ne.js":"3a39","./nl":"facd","./nl-be":"db29","./nl-be.js":"db29","./nl.js":"facd","./nn":"b84c","./nn.js":"b84c","./pa-in":"f3ff","./pa-in.js":"f3ff","./pl":"8d57","./pl.js":"8d57","./pt":"f260","./pt-br":"d2d4","./pt-br.js":"d2d4","./pt.js":"f260","./ro":"972c","./ro.js":"972c","./ru":"957c","./ru.js":"957c","./sd":"6784","./sd.js":"6784","./se":"ffff","./se.js":"ffff","./si":"eda5","./si.js":"eda5","./sk":"7be6","./sk.js":"7be6","./sl":"8155","./sl.js":"8155","./sq":"c8f3","./sq.js":"c8f3","./sr":"cf1e","./sr-cyrl":"13e9","./sr-cyrl.js":"13e9","./sr.js":"cf1e","./ss":"52bd","./ss.js":"52bd","./sv":"5fbd","./sv.js":"5fbd","./sw":"74dc","./sw.js":"74dc","./ta":"3de5","./ta.js":"3de5","./te":"5cbb","./te.js":"5cbb","./tet":"576c","./tet.js":"576c","./tg":"3b1b","./tg.js":"3b1b","./th":"10e8","./th.js":"10e8","./tl-ph":"0f38","./tl-ph.js":"0f38","./tlh":"cf75","./tlh.js":"cf75","./tr":"0e81","./tr.js":"0e81","./tzl":"cf51","./tzl.js":"cf51","./tzm":"c109","./tzm-latn":"b53d","./tzm-latn.js":"b53d","./tzm.js":"c109","./ug-cn":"6117","./ug-cn.js":"6117","./uk":"ada2","./uk.js":"ada2","./ur":"5294","./ur.js":"5294","./uz":"2e8c","./uz-latn":"010e","./uz-latn.js":"010e","./uz.js":"2e8c","./vi":"2921","./vi.js":"2921","./x-pseudo":"fd7e","./x-pseudo.js":"fd7e","./yo":"7f33","./yo.js":"7f33","./zh-cn":"5c3a","./zh-cn.js":"5c3a","./zh-hk":"49ab","./zh-hk.js":"49ab","./zh-tw":"90ea","./zh-tw.js":"90ea"};function n(e){var t=i(e);return a(t)}function i(e){var t=s[e];if(!(t+1)){var a=new Error("Cannot find module '"+e+"'");throw a.code="MODULE_NOT_FOUND",a}return t}n.keys=function(){return Object.keys(s)},n.resolve=i,e.exports=n,n.id="4678"},"56d7":function(e,t,a){"use strict";a.r(t);a("cadf"),a("551c"),a("097d");var s,n,i,r,l,c,o=a("2b0e"),d=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"container",attrs:{id:"app"}},[a("div",{staticClass:"row"},[a("div",{staticClass:"zeventig col trillingen"},[a("Trillingen",{attrs:{labols:e.trillingen.labels,datavalues:e.trillingen.data}})],1),a("div",{staticClass:"dertig col activities"},[a("Activities",{attrs:{labols:e.activities.labels,datavalues:e.activities.data}})],1)]),a("div",{staticClass:"row"},[a("div",{staticClass:"dertig col"},[a("Patient",{attrs:{patient:e.patient}})],1),a("div",{staticClass:"zeventig col"},[a("Dampening",{attrs:{labols:e.dampening.labels,datavalues:e.dampening.data}})],1)])])},u=[],f=(a("28a5"),a("e814")),b=a.n(f),j=(a("6b54"),a("bc3a")),p=a.n(j),h=a("1fca"),g={extends:h["b"],name:"Trillingen",props:["labols","datavalues"],methods:{renderDan:function(){this.renderChart({labels:this.labols,datasets:[{label:"Trillingen",data:this.datavalues,borderColor:"#1a7feb",backgroundColor:"rgba(0,0,0,0)"}]},{responsive:!0,maintainAspectRatio:!1,animation:!1,backgroundColor:null,scales:{yAxes:[{ticks:{min:0,suggestedMax:100,beginAtZero:!0,stepSize:5}}],xAxes:[{ticks:{min:10}}]}})}},watch:{datavalues:function(e,t){console.log("trilling props updated ",e,t),this.renderDan()}},mounted:function(){this.renderDan()}},m=g,v=a("2877"),y=Object(v["a"])(m,s,n,!1,null,null,null),k=y.exports,w={extends:h["a"],name:"Activities",props:["labols","datavalues"],methods:{renderDan:function(){this.renderChart({labels:this.labols,datasets:[{label:"Activities",data:this.datavalues,borderColor:"#1a7feb",backgroundColor:"#1a7feb"}]},{responsive:!0,maintainAspectRatio:!1,animation:!1,scales:{yAxes:[{ticks:{min:0,max:100,callback:function(e){return"".concat(e,"%")}},scaleLabel:{display:!0,labelString:"Percentage"}}]}})}},watch:{datavalues:function(e,t){console.log("trilling props updated ",e,t),this.renderDan()}},mounted:function(){this.renderDan()}},C=w,x=Object(v["a"])(C,i,r,!1,null,null,null),z=x.exports,_={extends:h["b"],name:"Dampenings",props:["labols","datavalues"],methods:{renderDan:function(){this.renderChart({labels:this.labols,datasets:[{label:"Luchtvochtigheid",data:this.datavalues,borderColor:"#1a7feb",backgroundColor:"rgba(0,0,0,0)"}]},{responsive:!0,maintainAspectRatio:!1,animation:!1,backgroundColor:null,scales:{yAxes:[{ticks:{suggestedMax:100,beginAtZero:!0,stepSize:5},scaleLabel:{display:!0,labelString:"Percentage"}}]}})}},watch:{datavalues:function(e,t){console.log("trilling props updated ",e,t),this.renderDan()}},mounted:function(){this.renderDan()}},D=_,O=Object(v["a"])(D,l,c,!1,null,null,null),A=O.exports,P=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"patient"},[a("div",[a("img",{attrs:{src:"https://www.finearttips.com/wp-content/uploads/2010/05/avatar.jpg"}}),a("h3",[e._v("Naam: "),a("span",[e._v(e._s(e.patient.fullname))])]),a("p",[e._v("Leeftijd: "),a("span",[e._v(e._s(e.patient.leeftijd))])]),a("p",[e._v("Initiele doses: "),a("span",[e._v(e._s(e.patient.initialdoses))])]),a("p",[e._v("BodyMass: "),a("span",[e._v(e._s(e.patient.bodymass))])])])])},S=[],$={name:"Patient",props:["patient"]},M=$,T=Object(v["a"])(M,P,S,!1,null,null,null),L=T.exports,E="http://nontwikkel.nl:9094",N={name:"root",data:function(){return{trillingen:{data:null,labels:null},activities:{labels:["liggen","staan"],data:[]},dampening:{labels:[],data:[]},patient:{}}},components:{Trillingen:k,Activities:z,Dampening:A,Patient:L},methods:{fetchData:function(){var e=this;p.a.all([p.a.get("".concat(E,"/measurements")),p.a.get("".concat(E,"/activities")),p.a.get("".concat(E,"/dampening")),p.a.get("".concat(E,"/patient"))]).then(p.a.spread(function(t,a,s,n){a.data.activities;e.updateActivityChart(a.data.activities),e.updateTrillingenChart(t.data.measurements),e.updateDampeningChart(s.data.dampening),e.$set(e,"patient",n.data.patients[0])}))},updateTrillingenChart:function(e){console.log("updateTrillingenChart",e);var t=10,a=e.slice(Math.max(e.length-t,1)).map(function(e){return e.aantaltrillingen}),s=e.slice(Math.max(e.length-t,1)).map(function(e){return new Date(b()(e.created)).toString()}).map(function(e){return e.split(" ")[4]});this.$set(this.trillingen,"labels",s),this.$set(this.trillingen,"data",a)},updateActivityChart:function(e){console.log("updateActivityChart",e);var t=e.filter(function(e){return e.staje}),a=e.filter(function(e){return!e.staje}),s=t.length,n=a.length,i=function(t,a){return t/e.length*100};if(console.log({stajewelCount:s,stajenietCount:n,stajewelPercent:i(n,s),stajenietPercent:i(s,n)}),s>n){var r=i(n,s);console.log({stajewelPercent:r}),this.$set(this.activities.data,0,r),this.$set(this.activities.data,1,100-r)}else{var l=i(s,n);console.log({stajenietPercent:l}),this.$set(this.activities.data,1,l),this.$set(this.activities.data,0,100-l)}},updateDampeningChart:function(e){var t=e.map(function(e){return e.luchtvochtigheid}),a=e.slice(Math.max(e.length-10,1)).map(function(e){return new Date(b()(e.created)).toString()}).map(function(e){return e.split(" ")[4]});this.$set(this.dampening,"data",t),this.$set(this.dampening,"labels",a)}},mounted:function(){this.fetchData();var e=5;window.setInterval(this.fetchData,1e3*e)}},R=N,q=Object(v["a"])(R,d,u,!1,null,null,null),G=q.exports;a("e848");o["a"].config.productionTip=!1,new o["a"]({render:function(e){return e(G)}}).$mount("#app")},e848:function(e,t,a){}});
//# sourceMappingURL=app.dfae3ea5.js.map