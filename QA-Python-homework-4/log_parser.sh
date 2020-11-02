#!/bin/bash
if [[ $# -eq 0 ]]
then
  echo "Provide log file or directory containing *.log files "
  exit 1
fi
source=$1
if [[ -d $source ]]
then
  echo "Looking for *.log files in $source"
  cd $source;
  files=`ls *.log`;
else
  files=$1;
fi

for i in $files;
do 
  if [[ -f $i ]]
  then
    echo -e "Started to process $i ..."
    output="/tmp/processed_$i.txt"
    echo -e "\nResult of processing $i\n">$output
    # Общее количество запросов
    echo -e "Total query amount: ">>$output
    grep -E "^\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" $i|wc -l  >> $output

    # кол-во GET,POST
    echo -e "\nStatistics on GET/POST methods: ">>$output
    grep -oE "GET|POST" $i |sort|uniq -c >>$output

    # Топ 10 самых больших по размеру запросов, должно быть видно url, код, число запросов
    echo -e "\nTop 10 queries by size: \n\t\t">>$output
    sort -t " " -nk10 -r $i|awk '{print $7" " $9 " " $10}'|uniq -u|head >>$output

    # Топ 10 запросов по количеству, которые завершились клиентской ошибкой, должно быть видно url, статус код, ip адрес
    # на каком урле клиент х получил больше всего 400-ых ошибок
    echo -e "\nTop 10 failed queries by ip, location: \n\t\t">>$output
    grep -E ".*\" 4[[:digit:]]{2} .+" $i |sort -t " " -nk1,9|awk '{print $1" " $7 " " $9}'|uniq -c|sort -t " " -rnk1|head >>$output

    # Топ 10 запросов серверных ошибок по размеру запроса, должно быть видно url, статус код, ip адрес
    echo -e "\nTop 10 failed queries by size: ">>$output
    grep -E ".*\" \b(4[[:digit:]]{2})\b .+" $i |sort -t " " -rnk10| awk '{print $1" " $7 " " $9}'|uniq -u|head >>$output
    echo -e "Processed $i and put results in $output";
  else
    echo -e "It looks like $i is not a text log file"
  fi
done


