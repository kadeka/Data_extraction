#!/bin/bash
echo "Start to run script"
	python 2.get_link_subMenu.py $line
echo "Get sub menu"
wait 20
echo "Start to get link product"
cat get_link_subMenu.csv | while read line 
do 
	python 3.get_link_pro.py $line 
wait 
done 
echo "Get link product"
wait 20
echo "Start to get product detail"
cat get_link_pro.csv | while read line
do 
	python 4.get_pro_detail.py $line
wait
done
echo"Get detail"