STARTTIME=$(date +%s)

sh ase.sh
ENDTIME=$(date +%s)

echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
