/usr/lib/spark/bin/spark-submit \
 --master yarn-client \
--executor-memory 10g  --executor-cores 2  --num-executors 10 \
--conf "spark.executor.extraJavaOptions=-XX:+PrintGCDetails -XX:+PrintGCTimeStamps" \
--conf spark.eventLog.enabled=true \
--conf spark.eventLog.dir=hdfs://memex/user/spark/applicationHistory \
--conf spark.yarn.historyServer.address=memex-spark-master.xdata.data-tactics-corp.com:18080 \
--conf spark.logConf=true \
--jars spark-examples_2.10-2.0.0-SNAPSHOT.jar,random-0.0.1-SNAPSHOT-shaded.jar  \
test_check_hdfs.py   \
$@
