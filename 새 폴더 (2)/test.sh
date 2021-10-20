StartTime=$(date +%s)


Python as.py
python ade.py
python ow.py
 

EndTime=$(date +%s)

echo "It takes $(($EndTime - $StartTime)) seconds to complete this task."
echo "Please wait 5 minutes...zzz..."
sleep 500






