loop 
areadsensor v 
if($v!=X) 
	print $v 
	rdata $v a b c 
	send $c 4 
end 
delay 1000