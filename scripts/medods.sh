#!/bin/bash
wget https://raw.githubusercontent.com/GreatMedivack/files/master/list.out

SERVER="${1:-DEFAULT_FILENAME}"
DATE=$(date +"_%d_%m_%y_")

cat list.out | grep "CrashLoopBackOff" >> qw
cat list.out | grep "Error" >> qw
cat list.out | grep "Running" >> wq

cut -d" " -f1 qw > fd1
cut -d" " -f1 wq > fs1
rm qw
rm wq

grep -E '^.{20}' fd1 | rev | cut -c18- | rev >  $SERVER$DATE$'failed'.out
grep 'redis*' fd1 >>  $SERVER$DATE$'failed'.out
grep -E '^.{20}' fs1 | rev | cut -c18- | rev >  $SERVER$DATE$'running'.out
grep 'db-mongo-0' fs1 >> $SERVER$DATE$'running'.out
grep 'db-postgres-0' fs1 >> $SERVER$DATE$'running'.out
rm fd1
rm fs1

data=$(date +"%d/%m/%y")
admin="$(whoami)"
unworking=$(sed -n '$=' $SERVER$DATE$'failed'.out)
working=$(sed -n '$=' $SERVER$DATE$'running'.out) 
touch $SERVER$DATE$'report'.out
chmod 666 $SERVER$DATE$'report'.out
echo "Количество работающих сервисов: $working" >> $SERVER$DATE$'report'.out
echo "Количество сервисов с ошибками: $unworking" >> $SERVER$DATE$'report'.out
echo "Имя системного пользователя: $admin" >> $SERVER$DATE$'report'.out
echo "Дата: $data" >> $SERVER$DATE$'report'.out

mkdir archives
zip -T $SERVER$DATE $SERVER$DATE*.out
mv $SERVER$DATE.zip archives/
rm *.out

exit 0
