loop 
wait 
read y 
print $y
rdata $y t cx cy
data c $cx $cy 
if($t>20) 
	mark 1
	send $c 
else 
	mark 0 
end