
RGraph=window.RGraph||{isrgraph:true,isRGraph:true,rgraph:true};RGraph.SVG=RGraph.SVG||{};(function(win,doc,undefined)
{RGraph.SVG.Scatter=function(conf)
{this.set=function(name,value)
{if(arguments.length===1&&typeof name==='object'){for(i in arguments[0]){if(typeof i==='string'){name=ret.name;value=ret.value;this.set(name,value);}}}else{var ret=RGraph.SVG.commonSetter({object:this,name:name,value:value});name=ret.name;value=ret.value;if(name==='colors'){this.originalColors=RGraph.SVG.arrayClone(value);this.colorsParsed=false;}
if(name==='labelsAboveSeperator'){name=labelsAboveSeparator;}
this.properties[name]=value;}
return this;};this.get=function(name)
{return this.properties[name];};this.id=conf.id;this.uid=RGraph.SVG.createUID();this.container=document.getElementById(this.id);this.layers={};this.svg=RGraph.SVG.createSVG({object:this,container:this.container});this.isRGraph=true;this.isrgraph=true;this.rgraph=true;this.width=Number(this.svg.getAttribute('width'));this.height=Number(this.svg.getAttribute('height'));this.data=conf.data;this.type='scatter';this.coords=[];this.coords2=[];this.colorsParsed=false;this.originalColors={};this.gradientCounter=1;this.sequential=0;this.line_groups=[];this.firstDraw=true;RGraph.SVG.OR.add(this);this.container.style.display='inline-block';this.properties={marginLeft:35,marginRight:35,marginTop:35,marginBottom:35,backgroundColor:null,backgroundImage:null,backgroundImageAspect:'none',backgroundImageStretch:true,backgroundImageOpacity:null,backgroundImageX:null,backgroundImageY:null,backgroundImageW:null,backgroundImageH:null,backgroundGrid:true,backgroundGridColor:'#ddd',backgroundGridLinewidth:1,backgroundGridHlines:true,backgroundGridHlinesCount:null,backgroundGridVlines:true,backgroundGridVlinesCount:null,backgroundGridBorder:true,backgroundGridDashed:false,backgroundGridDotted:false,backgroundGridDashArray:null,tickmarksStyle:'cross',tickmarksSize:7,colors:['black'],line:false,lineColors:null,lineLinewidth:1,errorbarsColor:'black',errorbarsLinewidth:1,errorbarsCapwidth:10,yaxis:true,yaxisTickmarks:true,yaxisTickmarksLength:3,yaxisColor:'black',yaxisScale:true,yaxisLabels:null,yaxisLabelsOffsetx:0,yaxisLabelsOffsety:0,yaxisLabelsCount:5,yaxisScaleUnitsPre:'',yaxisScaleUnitsPost:'',yaxisScaleStrict:false,yaxisScaleDecimals:0,yaxisScalePoint:'.',yaxisScaleThousand:',',yaxisScaleRound:false,yaxisScaleMax:null,yaxisScaleMin:0,yaxisScaleFormatter:null,yaxisTitle:'',yaxisTitleBold:null,yaxisTitleSize:null,yaxisTitleFont:null,yaxisTitleColor:null,yaxisTitleItalic:null,yaxisTitleOffsetx:0,yaxisTitleOffsety:0,yaxisTitleX:null,yaxisTitleY:null,yaxisTitleHalign:null,yaxisTitleValign:null,xaxis:true,xaxisTickmarks:true,xaxisTickmarksLength:5,xaxisLabels:null,xaxisLabelsPosition:'section',xaxisLabelsPositionEdgeTickmarksCount:10,xaxisColor:'black',xaxisLabelsOffsetx:0,xaxisLabelsOffsety:0,xaxisLabelsCount:10,xaxisLabelsFont:null,xaxisLabelsSize:null,xaxisLabelsColor:null,xaxisLabelsBold:null,xaxisLabelsItalic:null,xaxisScaleUnitsPre:'',xaxisScaleUnitsPost:'',xaxisScaleMax:null,xaxisScaleMin:0,xaxisScalePoint:'.',xaxisRound:false,xaxisScaleThousand:',',xaxisScaleDecimals:0,xaxisScaleFormatter:null,xaxisTitle:'',xaxisTitleBold:null,xaxisTitleSize:null,xaxisTitleFont:null,xaxisTitleColor:null,xaxisTitleItalic:null,xaxisTitleOffsetx:0,xaxisTitleOffsety:0,xaxisTitleX:null,xaxisTitleY:null,xaxisTitleHalign:null,xaxisTitleValign:null,textColor:'black',textFont:'Arial, Verdana, sans-serif',textSize:12,textBold:false,textItalic:false,text:null,labelsAboveFont:null,labelsAboveSize:null,labelsAboveBold:null,labelsAboveItalic:null,labelsAboveColor:null,labelsAboveBackground:'rgba(255,255,255,0.7)',labelsAboveBackgroundPadding:2,labelsAboveXUnitsPre:null,labelsAboveXUnitsPost:null,labelsAboveXPoint:null,labelsAboveXThousand:null,labelsAboveXFormatter:null,labelsAboveXDecimals:null,labelsAboveYUnitsPre:null,labelsAboveYUnitsPost:null,labelsAboveYPoint:null,labelsAboveYThousand:null,labelsAboveYFormatter:null,labelsAboveYDecimals:null,labelsAboveOffsetx:0,labelsAboveOffsety:-10,labelsAboveHalign:'center',labelsAboveValign:'bottom',labelsAboveSeparator:',',tooltipsOverride:null,tooltipsEffect:'fade',tooltipsCssClass:'RGraph_tooltip',tooltipsCss:null,tooltipsEvent:'mousemove',tooltipsFormattedThousand:',',tooltipsFormattedPoint:'.',tooltipsFormattedDecimals:0,tooltipsFormattedUnitsPre:'',tooltipsFormattedUnitsPost:'',tooltipsFormattedKeyColors:null,tooltipsFormattedKeyColorsShape:'square',tooltipsFormattedKeyLabels:[],tooltipsFormattedTableHeaders:null,tooltipsFormattedTableData:null,tooltipsPointer:true,tooltipsPositionStatic:true,highlightStroke:'rgba(0,0,0,0)',highlightFill:'rgba(255,255,255,0.7)',highlightLinewidth:1,title:'',titleX:null,titleY:null,titleHalign:'center',titleValign:null,titleSize:null,titleColor:null,titleFont:null,titleBold:null,titleItalic:null,titleSubtitle:null,titleSubtitleSize:null,titleSubtitleColor:'#aaa',titleSubtitleFont:null,titleSubtitleBold:null,titleSubtitleItalic:null,key:null,keyColors:null,keyOffsetx:0,keyOffsety:0,keyLabelsOffsetx:0,keyLabelsOffsety:-1,keyLabelsFont:null,keyLabelsSize:null,keyLabelsColor:null,keyLabelsBold:null,keyLabelsItalic:null,bubble:false,bubbleMaxValue:null,bubbleMaxRadius:null,bubbleColorsSolid:false,errorbars:null,errorbarsColor:'black',errorbarsLinewidth:1,errorbarsCapwidth:10,trendline:false,trendlineColors:['gray'],trendlineLinewidth:1,trendlineMargin:15,trendlineDashed:true,trendlineDotted:false,trendlineDashArray:null,trendlineClipping:null,outofbounds:true};RGraph.SVG.getGlobals(this);for(i in conf.options){if(typeof i==='string'){this.set(i,conf.options[i]);}}
if(this.data[0]&&!RGraph.SVG.isArray(this.data[0])){this.data=[];this.data[0]=conf.data;}
if(RGraph.SVG.FX&&typeof RGraph.SVG.FX.decorate==='function'){RGraph.SVG.FX.decorate(this);}
this.responsive=RGraph.SVG.responsive;RGraph.SVG.addCreateFunction(this);var properties=this.properties;if(typeof properties.xaxisScaleMin==='string'){properties.xaxisScaleMin=RGraph.SVG.parseDate(properties.xaxisScaleMin);}
if(typeof properties.xaxisScaleMax==='string'){properties.xaxisScaleMax=RGraph.SVG.parseDate(properties.xaxisScaleMax);}
for(var i=0;i<this.data.length;++i){for(var j=0;j<this.data[i].length;++j){if(typeof this.data[i][j].x==='string'){this.data[i][j].x=RGraph.SVG.parseDate(this.data[i][j].x);}}}
this.draw=function()
{RGraph.SVG.fireCustomEvent(this,'onbeforedraw');this.sequential=0;this.width=Number(this.svg.getAttribute('width'));this.height=Number(this.svg.getAttribute('height'));if(properties.xaxisLabels&&properties.xaxisLabels.length){if(typeof properties.xaxisLabels==='string'){properties.xaxisLabels=RGraph.SVG.arrayPad({array:[],length:properties.xaxisLabelsCount,value:properties.xaxisLabels});}
for(var i=0;i<properties.xaxisLabels.length;++i){properties.xaxisLabels[i]=RGraph.SVG.labelSubstitution({object:this,text:properties.xaxisLabels[i],index:i,value:this.data[0][i],decimals:properties.xaxisLabelsFormattedDecimals||0,unitsPre:properties.xaxisLabelsFormattedUnitsPre||'',unitsPost:properties.xaxisLabelsFormattedUnitsPost||'',thousand:properties.xaxisLabelsFormattedThousand||',',point:properties.xaxisLabelsFormattedPoint||'.'});}}
RGraph.SVG.createDefs(this);this.graphWidth=this.width-properties.marginLeft-properties.marginRight;this.graphHeight=this.height-properties.marginTop-properties.marginBottom;this.coords=[];this.coords2=[];RGraph.SVG.resetColorsToOriginalValues({object:this});this.parseColors();for(var ds=0,max=0;ds<this.data.length;++ds){for(var dp=0;dp<this.data[ds].length;++dp){max=Math.max(max,this.data[ds][dp].y+(this.data[ds][dp].errorbar?(typeof this.data[ds][dp].errorbar==='number'?this.data[ds][dp].errorbar:this.data[ds][dp].errorbar.max):0));}}
if(typeof properties.yaxisScaleMax==='number'){max=properties.yaxisScaleMax;}
if(properties.yaxisScaleMin==='mirror'||properties.yaxisScaleMin==='middle'||properties.yaxisScaleMin==='center'){var mirrorScale=true;properties.yaxisScaleMin=0;}
this.scale=RGraph.SVG.getScale({object:this,numlabels:properties.yaxisLabelsCount,unitsPre:properties.yaxisScaleUnitsPre,unitsPost:properties.yaxisScaleUnitsPost,max:max,min:properties.yaxisScaleMin,point:properties.yaxisScalePoint,round:properties.yaxisScaleRound,thousand:properties.yaxisScaleThousand,decimals:properties.yaxisScaleDecimals,strict:typeof properties.yaxisScaleMax==='number',formatter:properties.yaxisScaleFormatter});if(mirrorScale){this.scale=RGraph.SVG.getScale({object:this,numlabels:properties.yaxisLabelsCount,unitsPre:properties.yaxisScaleUnitsPre,unitsPost:properties.yaxisScaleUnitsPost,max:this.scale.max,min:this.scale.max* -1,point:properties.yaxisScalePoint,round:false,thousand:properties.yaxisScaleThousand,decimals:properties.yaxisScaleDecimals,strict:typeof properties.yaxisScaleMax==='number',formatter:properties.yaxisScaleFormatter});}
this.max=this.scale.max;this.min=this.scale.min;properties.yaxisScaleMax=this.scale.max;properties.yaxisScaleMin=this.scale.min;RGraph.SVG.drawBackground(this);RGraph.SVG.drawXAxis(this);RGraph.SVG.drawYAxis(this);var dataset_group=RGraph.SVG.create({svg:this.svg,type:'g',parent:this.svg.all,attr:{className:'scatter_datasets_'+this.uid}});for(var i=0;i<this.data.length;++i){var group=RGraph.SVG.create({svg:this.svg,type:'g',parent:this.svg.all,attr:{id:'scatter_line_'+i+this.uid}});this.line_groups[i]=group;this.drawPoints({index:i,data:this.data[i],group:dataset_group});if(properties.line===true||(typeof properties.line==='object'&&properties.line[i]===true)){this.drawLine({index:i,coords:this.coords2[i],});}}
if(properties.trendline){for(var i=0;i<this.data.length;++i){if(properties.trendline===true||(typeof properties.trendline==='object'&&properties.trendline[i]===true)){this.drawTrendline(i);}}}
if(typeof properties.key!==null&&RGraph.SVG.drawKey){RGraph.SVG.drawKey(this);}else if(!RGraph.SVG.isNull(properties.key)){alert('The drawKey() function does not exist - have you forgotten to include the key library?');}
RGraph.SVG.addCustomText(this);if(this.firstDraw){this.firstDraw=false;RGraph.SVG.fireCustomEvent(this,'onfirstdraw');}
RGraph.SVG.fireCustomEvent(this,'ondraw');return this;};this.drawPoints=function(opt)
{var index=opt.index,data=opt.data,group=opt.group;if(!this.coords2[index]){this.coords2[index]=[];}
var group=RGraph.SVG.create({svg:this.svg,type:'g',parent:group,attr:{className:'scatter_dataset_'+index+'_'+this.uid}});for(var i=0;i<data.length;++i){var point=data[i];if(typeof point.x==='number'&&typeof point.y==='number'){var ret=this.drawSinglePoint({dataset:data,datasetIdx:index,point:point,index:i,group:group,sequential:this.sequential});this.coords.push({x:ret.x,y:ret.y,z:ret.size,type:ret.type,element:ret.mark,object:this});this.coords2[index][i]={x:ret.x,y:ret.y,z:ret.size,type:ret.type,element:ret.mark,object:this};this.sequential++}
if((typeof data[i].tooltip==='string'&&data[i].tooltip)||(typeof data[i].tooltip==='number')||(typeof properties.tooltips==='string')){data[i].tooltip=String(data[i].tooltip);if(properties.tooltipsEvent!=='mousemove'){properties.tooltipsEvent='click';}
if(!group_tooltip_hotspots){var group_tooltip_hotspots=RGraph.SVG.create({svg:this.svg,parent:this.svg.all,type:'g',attr:{className:'rgraph-scatter-tooltip-hotspots'}});}
var rect=RGraph.SVG.create({svg:this.svg,parent:this.svg.all,type:'rect',parent:group_tooltip_hotspots,attr:{x:ret.x-(ret.size/2),y:ret.y-(ret.size/2),width:ret.size,height:ret.size,fill:'transparent',stroke:'transparent','stroke-width':0},style:{cursor:'pointer'}});ret.mark.hotspot=rect;(function(dataset,index,seq,obj)
{rect.addEventListener(properties.tooltipsEvent,function(e)
{var tooltip=RGraph.SVG.REG.get('tooltip');if(tooltip&&tooltip.__dataset__===dataset&&tooltip.__index__===index){return;}
obj.removeHighlight();RGraph.SVG.tooltip({object:obj,dataset:dataset,index:index,sequentialIndex:seq,text:typeof properties.tooltips==='string'?properties.tooltips:obj.data[dataset][index].tooltip,event:e});if(RGraph.SVG.REG.get('tooltip')){obj.highlight(this);}},false);if(properties.tooltipsEvent==='click'){rect.addEventListener('mousemove',function(e)
{e.target.style.cursor='pointer';},false);}}(index,i,this.sequential-1,this));}}};this.drawSinglePoint=function(opt)
{var dataset=opt.dataset,datasetIdx=opt.datasetIdx,seq=opt.sequential,point=opt.point,index=opt.index,valueX=opt.point.x,valueY=opt.point.y,conf=opt.point||{},group=opt.group,coordX=opt.coordx=this.getXCoord(valueX),coordY=opt.coordy=this.getYCoord(valueY);if(conf.labelsAbove){var above=true;}else if(conf.labelAbove){var above=true;}else if(conf.above){var above=true;}
if(typeof conf.type==='undefined'&&typeof conf.shape!=='undefined'){conf.type=conf.shape;}
if(typeof conf.type!=='string'){if(typeof properties.tickmarksStyle==='string'){conf.type=properties.tickmarksStyle;}else if(typeof properties.tickmarksStyle==='object'&&typeof properties.tickmarksStyle[datasetIdx]==='string'){conf.type=properties.tickmarksStyle[datasetIdx];}else{conf.type='cross';}}
if(typeof conf.size!=='number'&&typeof properties.tickmarksSize==='number'){conf.size=properties.tickmarksSize;}else if(typeof conf.size!=='number'&&typeof properties.tickmarksSize==='object'&&typeof properties.tickmarksSize[datasetIdx]==='number'){conf.size=properties.tickmarksSize[datasetIdx];}
if(typeof conf.color==='string'){}else if(typeof properties.colors[datasetIdx]==='string'){conf.color=properties.colors[datasetIdx];}else{conf.color='black';}
if(typeof conf.opacity==='undefined'){conf.opacity=1;}else if(typeof conf.opacity==='number'){}
properties.errorbars=[];for(var ds=0,max=0;ds<this.data.length;++ds){for(var idx=0;idx<this.data[ds].length;++idx){properties.errorbars.push(this.data[ds][idx].errorbar);}}
this.drawErrorbar({object:this,dataset:datasetIdx,index:index,group:group,sequential:seq,x:coordX,y:coordY,valueX:valueX,valueY:valueY,parent:group});if(properties.bubble){this.drawBubble(opt,conf);}
switch(conf.type){case'image:'+conf.type.substr(6):var src=conf.type.substr(6);var img=new Image();img.src=src;var mark=RGraph.SVG.create({svg:this.svg,type:'image',parent:group,attr:{preserveAspectRatio:'xMidYMid meet','xlink:href':src}});img.onload=function()
{var x=coordX-(img.width/2),y=coordY-(img.height/2),w=img.width,h=img.height;mark.setAttribute('x',x);mark.setAttribute('y',y);mark.setAttribute('width',w);mark.setAttribute('height',h);if(mark&&mark.hotspot){mark.hotspot.setAttribute('x',x);mark.hotspot.setAttribute('y',y);mark.hotspot.setAttribute('width',w);mark.hotspot.setAttribute('height',h);}};break;case'triangle':var mark=RGraph.SVG.create({svg:this.svg,type:'path',parent:group,attr:{d:'M {1} {2} L {3} {4} L {5} {6}'.format(coordX-(conf.size/2),coordY+(conf.size/2),coordX,coordY-(conf.size/2),coordX+(conf.size/2),coordY+(conf.size/2)),fill:conf.color,'fill-opacity':conf.opacity}});break;case'plus':var mark=RGraph.SVG.create({svg:this.svg,type:'path',parent:group,attr:{d:'M {1} {2} L {3} {4} M {5} {6} L {7} {8}'.format(coordX-(conf.size/2),coordY,coordX+(conf.size/2),coordY,coordX,coordY-(conf.size/2),coordX,coordY+(conf.size/2)),stroke:conf.color,'stroke-opacity':conf.opacity}});break;case'square':case'rect':var mark=RGraph.SVG.create({svg:this.svg,type:'rect',parent:group,attr:{x:coordX-(conf.size/2),y:coordY-(conf.size/2),width:conf.size,height:conf.size,fill:conf.color,'fill-opacity':conf.opacity}});break;case'dot':case'circle':var mark=RGraph.SVG.create({svg:this.svg,type:'circle',parent:group,attr:{cx:coordX,cy:coordY,r:conf.size/2,fill:conf.color,'fill-opacity':conf.opacity}});break;case'cross':default:var mark=RGraph.SVG.create({svg:this.svg,type:'path',parent:group,attr:{d:'M {1} {2} L {3} {4} M {5} {6} L {7} {8}'.format(coordX-(conf.size/2),coordY-(conf.size/2),coordX+(conf.size/2),coordY+(conf.size/2),coordX-(conf.size/2),coordY+(conf.size/2),coordX+(conf.size/2),coordY-(conf.size/2)),stroke:conf.color,'stroke-opacity':conf.opacity}});break;}
if(typeof conf.above==='string'||(typeof conf.above!=='string'&&conf.above)){this.drawLabelsAbove({point:conf,coordX:coordX,coordY:coordY});}
mark.setAttribute('data-index',index);mark.setAttribute('data-dataset',datasetIdx);mark.setAttribute('data-original-opacity',conf.opacity);mark.setAttribute('data-original-color',conf.color);mark.setAttribute('data-original-coordx',coordX);mark.setAttribute('data-original-coordy',coordY);mark.setAttribute('data-size',conf.size);mark.setAttribute('data-sequential',seq);mark.setAttribute('data-type',conf.type);return{x:coordX,y:coordY,size:conf.type.substr(0,6)==='image:'?img.width:conf.size,mark:mark,type:conf.type};};this.drawBubble=function(opt,conf)
{var size=(conf.z/properties.bubbleMaxValue)*properties.bubbleMaxRadius;var color=RGraph.SVG.parseColorRadial({object:this,color:properties.bubbleColorsSolid?conf.color:'Gradient(white:'+conf.color+')',cx:opt.coordx+(size/4),cy:opt.coordy-(size/4),fx:opt.coordx+(size/4),fy:opt.coordy-(size/4),r:size*1.5});var circle=RGraph.SVG.create({svg:this.svg,type:'circle',attr:{cx:opt.coordx,cy:opt.coordy,r:size,fill:color,'fill-opacity':conf.opacity}});circle.setAttribute('data-index',opt.index);circle.setAttribute('data-dataset',opt.datasetIdx);circle.setAttribute('data-original-opacity',conf.opacity);circle.setAttribute('data-original-color',conf.color);circle.setAttribute('data-original-coordx',opt.coordx);circle.setAttribute('data-original-coordy',opt.coordy);circle.setAttribute('data-size',size);circle.setAttribute('data-sequential',opt.sequential);circle.setAttribute('data-type','bubble');return{x:opt.coordx,y:opt.coordy,z:opt.coordz};};this.drawLine=function(opt)
{var linewidth=1,color='black';if(typeof properties.lineLinewidth==='object'&&typeof properties.lineLinewidth[opt.index]==='number'){linewidth=properties.lineLinewidth[opt.index];}else if(typeof properties.lineLinewidth==='number'){linewidth=properties.lineLinewidth;}else{linewidth=1;}
if(!RGraph.SVG.isNull(properties.lineColors)&&properties.lineColors&&properties.lineColors[opt.index]){color=properties.lineColors[opt.index];}else if(!RGraph.SVG.isNull(properties.colors)&&properties.colors.length&&typeof properties.colors[opt.index]==='string'){color=properties.colors[opt.index];}else if(typeof properties.lineColors==='string'){color=properties.lineColors;}else{color='black';}
for(var i=0,path='';i<this.coords2[opt.index].length;++i){path+='{1} {2} {3} '.format(i===0?'M':'L',this.coords2[opt.index][i].x,this.coords2[opt.index][i].y);}
RGraph.SVG.create({svg:this.svg,type:'path',parent:this.line_groups[opt.index],attr:{d:path,fill:'transparent',stroke:color,'stroke-width':linewidth,'stroke-linecap':'round','stroke-linejoin':'round'}});};this.getXCoord=function(value)
{var x;if(value>properties.xaxisScaleMax){return null;}
if(value<properties.xaxisScaleMin){return null;}
x=((value-properties.xaxisScaleMin)/(properties.xaxisScaleMax-properties.xaxisScaleMin));x*=(this.width-properties.marginLeft-properties.marginRight);x=properties.marginLeft+x;return x;};this.getYCoord=function(value)
{if(value>this.scale.max&&properties.outofbounds===false){return null;}
var y,xaxispos=properties.xaxispos;if(value<this.scale.min&&properties.outofbounds===false){return null;}
y=((value-this.scale.min)/(this.scale.max-this.scale.min));y*=(this.height-properties.marginTop-properties.marginBottom);y=this.height-properties.marginBottom-y;return y;};this.highlight=function(rect)
{rect.setAttribute('stroke',properties.highlightStroke);rect.setAttribute('stroke-width',properties.highlightLinewidth);rect.setAttribute('fill',properties.highlightFill);RGraph.SVG.REG.set('highlight',rect);};this.drawLabelsAbove=function(opt)
{var conf=opt.point,coordX=opt.coordX,coordY=opt.coordY;if(typeof conf.above==='string'){var str=conf.above;}else{conf.x=RGraph.SVG.numberFormat({object:this,num:conf.x.toFixed(properties.labelsAboveXDecimals),prepend:typeof properties.labelsAboveXUnitsPre==='string'?properties.labelsAboveXUnitsPre:null,append:typeof properties.labelsAboveXUnitsPost==='string'?properties.labelsAboveXUnitsPost:null,point:typeof properties.labelsAboveXPoint==='string'?properties.labelsAboveXPoint:null,thousand:typeof properties.labelsAboveXThousand==='string'?properties.labelsAboveXThousand:null,formatter:typeof properties.labelsAboveXFormatter==='function'?properties.labelsAboveXFormatter:null});conf.y=RGraph.SVG.numberFormat({object:this,num:conf.y.toFixed(properties.labelsAboveYDecimals),prepend:typeof properties.labelsAboveYUnitsPre==='string'?properties.labelsAboveYUnitsPre:null,append:typeof properties.labelsAboveYUnitsPost==='string'?properties.labelsAboveYUnitsPost:null,point:typeof properties.labelsAboveYPoint==='string'?properties.labelsAboveYPoint:null,thousand:typeof properties.labelsAboveYThousand==='string'?properties.labelsAboveYThousand:null,formatter:typeof properties.labelsAboveYFormatter==='function'?properties.labelsAboveYFormatter:null});var str='{1}{2}{3}'.format(conf.x,properties.labelsAboveSeparator,conf.y);}
var textConf=RGraph.SVG.getTextConf({object:this,prefix:'labelsAbove'});RGraph.SVG.text({object:this,parent:this.svg.all,tag:'labels.above',text:str,x:parseFloat(coordX)+properties.labelsAboveOffsetx,y:parseFloat(coordY)+properties.labelsAboveOffsety,halign:properties.labelsAboveHalign,valign:properties.labelsAboveValign,font:textConf.font,size:textConf.size,bold:textConf.bold,italic:textConf.italic,color:textConf.color,background:properties.labelsAboveBackground||null,padding:properties.labelsAboveBackgroundPadding||0});};this.parseColors=function()
{if(!Object.keys(this.originalColors).length){this.originalColors={colors:RGraph.SVG.arrayClone(properties.colors),backgroundGridColor:RGraph.SVG.arrayClone(properties.backgroundGridColor),highlightFill:RGraph.SVG.arrayClone(properties.highlightFill),backgroundColor:RGraph.SVG.arrayClone(properties.backgroundColor)}}
var colors=properties.colors;if(colors&&!properties.bubble){for(var i=0;i<colors.length;++i){colors[i]=RGraph.SVG.parseColorLinear({object:this,color:colors[i]});}}
properties.backgroundGridColor=RGraph.SVG.parseColorLinear({object:this,color:properties.backgroundGridColor});properties.highlightFill=RGraph.SVG.parseColorLinear({object:this,color:properties.highlightFill});properties.backgroundColor=RGraph.SVG.parseColorLinear({object:this,color:properties.backgroundColor});};this.on=function(type,func)
{if(type.substr(0,2)!=='on'){type='on'+type;}
RGraph.SVG.addCustomEventListener(this,type,func);return this;};this.exec=function(func)
{func(this);return this;};this.removeHighlight=function()
{var highlight=RGraph.SVG.REG.get('highlight');if(highlight){highlight.setAttribute('fill','transparent');RGraph.SVG.REG.set('highlight',null);}};this.drawErrorbar=function(opt)
{var max=RGraph.SVG.getErrorbarsMaxValue({object:this,index:opt.sequential});var min=RGraph.SVG.getErrorbarsMinValue({object:this,index:opt.sequential});if(!max&&!min){return;}
var linewidth=RGraph.SVG.getErrorbarsLinewidth({object:this,index:opt.sequential}),color=RGraph.SVG.getErrorbarsColor({object:this,index:opt.sequential}),capwidth=RGraph.SVG.getErrorbarsCapWidth({object:this,index:opt.sequential}),halfCapWidth=capwidth/2;if(max!==0||min!==0){var y1=this.getYCoord(opt.valueY+max)
y2=this.getYCoord(opt.valueY-min);var errorbarLine=RGraph.SVG.create({svg:this.svg,type:'line',parent:opt.parent,attr:{x1:opt.x,y1:opt.y,x2:opt.x,y2:y1,stroke:color,'stroke-width':linewidth}});var errorbarCap=RGraph.SVG.create({svg:this.svg,type:'line',parent:opt.parent,attr:{x1:opt.x-halfCapWidth,y1:y1,x2:opt.x+halfCapWidth,y2:y1,stroke:color,'stroke-width':linewidth}});}
if(typeof min==='number'){var errorbarLine=RGraph.SVG.create({svg:this.svg,type:'line',parent:opt.parent,attr:{x1:opt.x,y1:opt.y,x2:opt.x,y2:y2,stroke:color,'stroke-width':linewidth}});var errorbarCap=RGraph.SVG.create({svg:this.svg,type:'line',parent:opt.parent,attr:{x1:opt.x-halfCapWidth,y1:y2,x2:opt.x+halfCapWidth,y2:y2,stroke:color,'stroke-width':linewidth}});}};this.tooltipSubstitutions=function(opt)
{var indexes=RGraph.SVG.sequentialIndexToGrouped(opt.index,this.data),dataset=indexes[0],index=indexes[1];return{index:index,dataset:dataset,sequentialIndex:opt.index,value:this.data[dataset][index].y,values:[this.data[dataset][index].y]};};this.tooltipsFormattedCustom=function(specific,index,colors)
{var color=this.data[specific.dataset][specific.index].color?this.data[specific.dataset][specific.index].color:properties.colorsDefault;if(properties.tooltipsFormattedKeyColors&&properties.tooltipsFormattedKeyColors[specific.dataset]){color=properties.tooltipsFormattedKeyColors[specific.dataset];}
var label=properties.tooltipsFormattedKeyLabels[specific.dataset]?properties.tooltipsFormattedKeyLabels[specific.dataset]:'';return{label:label,color:color};};this.positionTooltipStatic=function(args)
{var obj=args.object,e=args.event,tooltip=args.tooltip,index=args.index,svgXY=RGraph.SVG.getSVGXY(obj.svg),coords=this.coords[args.index];args.tooltip.style.left=(svgXY[0]
+coords.x
-(tooltip.offsetWidth/2))+'px';args.tooltip.style.top=(svgXY[1]
+coords.y
-tooltip.offsetHeight
-15)+'px';};this.drawTrendline=function(dataset)
{var colors=properties.trendlineColors,linewidth=properties.trendlineLinewidth,margin=properties.trendlineMargin;if(RGraph.SVG.isString(properties.trendlineColor)){colors=[properties.trendlineColor];}
if(typeof colors==='object'&&colors[dataset]){color=colors[dataset];}else if(typeof color==='object'){color='gray';}
if(typeof linewidth==='object'&&typeof linewidth[dataset]==='number'){linewidth=linewidth[dataset];}else if(typeof linewidth==='object'){linewidth=1;}
if(typeof margin==='object'&&typeof margin[dataset]==='number'){margin=margin[dataset];}else if(typeof margin==='object'){margin=25;}
for(var i=0,totalX=0,totalY=0;i<this.data[dataset].length;++i){totalX+=this.data[dataset][i].x;totalY+=this.data[dataset][i].y;}
var averageX=totalX/this.data[dataset].length;var averageY=totalY/this.data[dataset].length;for(var i=0,xCoordMinusAverageX=[],yCoordMinusAverageY=[],valuesMultiplied=[],xCoordMinusAverageSquared=[];i<this.data[dataset].length;++i){xCoordMinusAverageX[i]=this.data[dataset][i].x-averageX;yCoordMinusAverageY[i]=this.data[dataset][i].y-averageY;valuesMultiplied[i]=xCoordMinusAverageX[i]*yCoordMinusAverageY[i];xCoordMinusAverageSquared[i]=xCoordMinusAverageX[i]*xCoordMinusAverageX[i];}
var sumOfValuesMultiplied=RGraph.SVG.arraySum(valuesMultiplied);var sumOfXCoordMinusAverageSquared=RGraph.SVG.arraySum(xCoordMinusAverageSquared);var m=sumOfValuesMultiplied/sumOfXCoordMinusAverageSquared;var b=averageY-(m*averageX);coords=[[properties.xaxisScaleMin,m*properties.xaxisScaleMin+b],[properties.xaxisScaleMax,m*properties.xaxisScaleMax+b]];var strokeDasharray=''
if(properties.trendlineDashed){strokeDasharray='4,4';}
if(properties.trendlineDotted){strokeDasharray='1, 4';}
if(!RGraph.SVG.isNull(properties.trendlineDashArray)&&typeof properties.trendlineDashArray==='object'){strokeDasharray=String(properties.trendlineDashArray).replace(/[|]/,'');}
for(var i=0,xValues=[],yValues=[];i<this.data[dataset].length;++i){if(typeof this.data[dataset][i].x==='number'){xValues.push(this.data[dataset][i].x);}
if(typeof this.data[dataset][i].y==='number'){yValues.push(this.data[dataset][i].y);}}
var x1=RGraph.SVG.arrayMin(xValues);var y1=RGraph.SVG.arrayMin(yValues);var x2=RGraph.SVG.arrayMax(xValues);var y2=RGraph.SVG.arrayMax(yValues);x1=this.getXCoord(x1);y1=this.getYCoord(y1,properties.outofbounds);x2=this.getXCoord(x2);y2=this.getYCoord(y2,properties.outofbounds);var clippath=RGraph.SVG.create({svg:this.svg,parent:this.svg.defs,type:'clipPath',attr:{id:'trendline-clippath-dataset-'+dataset}});RGraph.SVG.create({svg:this.svg,parent:clippath,type:'rect',attr:{x:properties.trendlineClipping===false?properties.marginLeft:x1-margin,y:properties.trendlineClipping===false?properties.marginTop:y2-margin,width:properties.trendlineClipping===false?(this.width-properties.marginLeft-properties.marginRight):x2-x1+margin+margin,height:properties.trendlineClipping===false?this.height-properties.marginTop-properties.marginBottom:y1-y2+margin+margin}});var line=RGraph.SVG.create({svg:this.svg,parent:this.svg.all,type:'path',attr:{d:'M{1} {2} L{3} {4}'.format(this.getXCoord(coords[0][0]),this.getYCoord(coords[0][1]),this.getXCoord(coords[1][0]),this.getYCoord(coords[1][1])),stroke:color,fill:'none','stroke-width':linewidth,'stroke-dasharray':strokeDasharray,'stroke-linecap':'round','clip-path':'url(#trendline-clippath-dataset-'+dataset+')'}});};return this;};})(window,document);