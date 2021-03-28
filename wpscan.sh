for i in $(cat $1)
do
URL=("${i}")
for x in "${URL[@]}"
do
wpscan --url $x --api-token $(cat $2) --wp-content-dir / --ignore-main-redirect
sleep 5
done
done
