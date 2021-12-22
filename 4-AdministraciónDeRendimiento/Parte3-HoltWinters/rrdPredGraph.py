import time
import rrdtool
from path import *

title="Deteccion de comportamiento anomalo"
fname=rrdpath+rrdname
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 8000
DatosAyer=begDate - 8640
FinAyer=endDate - 8640
#rrdtool.tune(rrdname, '--alpha', '0.1')
ret = rrdtool.graph(pngpath+"pred.png",
                        '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                        "--vertical-label=Carga CPU Predict/s",
                        '--slope-mode',
                        "DEF:obs=" + fname + ":CPUload:AVERAGE",
                        "DEF:obsAyer=" + fname + ":CPUload:AVERAGE:start="+str(DatosAyer)+":end="+str(FinAyer),
                        "DEF:pred=" + fname + ":CPUload:HWPREDICT",
                        "DEF:dev=" + fname + ":CPUload:DEVPREDICT",
                        "DEF:fail=" + fname + ":CPUload:FAILURES",
                        'SHIFT:obsAyer:86400',
                    #"RRA:DEVSEASONAL:1d:0.1:2",
                    #"RRA:DEVPREDICT:5d:5",
                    #"RRA:FAILURES:1d:7:9:5""
                        "CDEF:scaledobs=obs,8,*",
                        "CDEF:scaledobsAyer=obsAyer,8,*",
                        "CDEF:upper=pred,dev,2,*,+",
                        "CDEF:lower=pred,dev,2,*,-",
                        "CDEF:scaledupper=upper,8,*",
                        "CDEF:scaledlower=lower,8,*",
                        "CDEF:scaledpred=pred,8,*",
                    "TICK:fail#FDD017:1.0: Fallas",
                    "AREA:scaledobsAyer#9C9C9C:Ayer",
                    "LINE3:scaledobs#00FF00:In CPU",
                    "LINE1:scaledpred#FF00FF:Prediccion",
                    #"LINE1:outoctets#0000FF:Out traffic",
                    "LINE1:scaledupper#ff0000:Upper Bound Average CPU in",
                    "LINE1:scaledlower#0000FF:Lower Bound Average CPU in",
                    "TICK:fail#FDD017:1.0:Fallas"
                    )
