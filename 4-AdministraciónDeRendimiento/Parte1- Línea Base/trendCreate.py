import rrdtool
ret = rrdtool.create("/home/eric/ASR/Practicas/Problema1_2/4-AdministraciónDeRendimiento/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:600:U:U",
                     #"DS:RAMload:GAUGE:600:U:U",
                     "RRA:AVERAGE:0.5:1:60",
            #RRA:HWPREDICT:rows:alpha:beta:seasonal period[:rra - num]
                     "RRA:HWPREDICT:100:0.1:0.0035:20:3",
              #RRA:SEASONAL:seasonal period:gamma:rra-num
                     "RRA:SEASONAL:20:0.1:2",
              #RRA:DEVSEASONAL:seasonal period:gamma:rra-num
                     "RRA:DEVSEASONAL:20:0.1:2",
                #RRA:DEVPREDICT:rows:rra-num
                     "RRA:DEVPREDICT:100:4",
            #RRA:FAILURES:rows:threshold:window length:rra-num
                     "RRA:FAILURES:100:7:9:4")
if ret:
    print (rrdtool.error())
