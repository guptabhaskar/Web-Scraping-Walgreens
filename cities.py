def func(s):
	while(s.find("TX")!=-1):
		t=s.find("TX")
		s=s[:t-1]+s[t+2:]
	s="\""+s[:-1]+"\""
	s1=""
	while(s.find(",")):
		t=s.find(",")
		s1=s1+s[:t]+"\""+","+"\""
		s=s[t+1:]
		print(s1)
	s1=s1+"\""+s
	print(s1)
s="ABILENE, TXALAMO, TXALICE, TXALLEN, TXALVIN, TXAMARILLO, TXANGLETON, TXANTHONY, TXARANSAS PASS, TXARLINGTON, TXATHENS, TXAUBREY, TXAUSTIN, TXAZLE, TXBASTROP, TXBAY CITY, TXBAYTOWN, TXBEAUMONT, TXBEDFORD, TXBEE CAVE, TXBEEVILLE, TXBELLAIRE, TXBELTON, TXBENBROOK, TXBEVERLY HILLS, TXBOERNE, TXBRENHAM, TXBRIDGE CITY, TXBROWNSVILLE, TXBROWNWOOD, TXBRYAN, TXBUDA, TXBURLESON, TXBURNET, TXCARROLLTON, TXCEDAR HILL, TXCEDAR PARK, TXCHANNELVIEW, TXCLEBURNE, TXCLEVELAND, TXCLUTE, TXCOLLEGE STATION, TXCOLLEYVILLE, TXCONROE, TXCONVERSE, TXCOPPELL, TXCOPPERAS COVE, TXCORINTH, TXCORPUS CHRISTI, TXCROSBY, TXCROWLEY, TXCYPRESS, TXDALLAS, TXDAYTON, TXDEER PARK, TXDENTON, TXDESOTO, TXDICKINSON, TXDRIPPING SPRINGS, TXDUNCANVILLE, TXEAGLE PASS, TXEDINBURG, TXEL CAMPO, TXEL PASO, TXENNIS, TXFARMERS BRANCH, TXFLOWER MOUND, TXFORNEY, TXFORT WORTH, TXFREDERICKSBURG, TXFRESNO, TXFRIENDSWOOD, TXFRISCO, TXGALVESTON, TXGARLAND, TXGATESVILLE, TXGEORGETOWN, TXGRANBURY, TXGRAND PRAIRIE, TXGRAPEVINE, TXGREENVILLE, TXGROVES, TXHALTOM CITY, TXHARKER HEIGHTS, TXHARLINGEN, TXHENDERSON, TXHIGHLAND VILLAGE, TXHORIZON CITY, TXHOUSTON, TXHUDSON OAKS, TXHUMBLE, TXHUNTSVILLE, TXHURST, TXHUTTO, TXIRVING, TXJACINTO CITY, TXJACKSONVILLE, TXJASPER, TXKATY, TXKELLER, TXKEMAH, TXKERRVILLE, TXKILGORE, TXKILLEEN, TXKINGSVILLE, TXKINGWOOD, TXKYLE, TXLA MARQUE, TXLA PORTE, TXLAKE JACKSON, TXLAKE WORTH, TXLAKEWAY, TXLANCASTER, TXLAREDO, TXLEAGUE CITY, TXLEANDER, TXLEWISVILLE, TXLITTLE ELM, TXLIVINGSTON, TXLOCKHART, TXLONGVIEW, TXLUBBOCK, TXLUFKIN, TXLUMBERTON, TXMAGNOLIA, TXMANSFIELD, TXMARBLE FALLS, TXMARSHALL, TXMCALLEN, TXMCKINNEY, TXMEADOWS PLACE, TXMESQUITE, TXMIDLAND, TXMIDLOTHIAN, TXMINERAL WELLS, TXMISSION, TXMISSOURI CITY, TXMONTGOMERY, TXMOUNT PLEASANT, TXMURPHY, TXNACOGDOCHES, TXNEW BRAUNFELS, TXNEW CANEY, TXNORTH RICHLAND HILLS, TXODESSA, TXORANGE, TXPALESTINE, TXPALMHURST, TXPALMVIEW, TXPARIS, TXPASADENA, TXPEARLAND, TXPFLUGERVILLE, TXPINEHURST, TXPLANO, TXPLEASANTON, TXPORT ARTHUR, TXPORT ISABEL, TXPORT LAVACA, TXPORT NECHES, TXPORTER, TXPORTLAND, TXRED OAK, TXRICHARDSON, TXRICHMOND, TXROCKPORT, TXROCKWALL, TXROSENBERG, TXROUND ROCK, TXROWLETT, TXSACHSE, TXSAGINAW, TXSAN ANGELO, TXSAN ANTONIO, TXSAN JUAN, TXSAN MARCOS, TXSCHERTZ, TXSEAGOVILLE, TXSEALY, TXSEGUIN, TXSHAVANO PARK, TXSHERMAN, TXSILSBEE, TXSOCORRO, TXSOUTHLAKE, TXSPRING, TXSPRING BRANCH, TXSTEPHENVILLE, TXSUGAR LAND, TXSULPHUR SPRINGS, TXTAYLOR, TXTEMPLE, TXTEXARKANA, TXTEXAS CITY, TXTHE COLONY, TXTHE WOODLANDS, TXTOMBALL, TXTROPHY CLUB, TXTYLER, TXUVALDE, TXVICTORIA, TXVIDOR, TXWACO, TXWATAUGA, TXWAXAHACHIE, TXWEATHERFORD, TXWESLACO, TXWEST COLUMBIA, TXWEST LAKE HILLS, TXWICHITA FALLS, TX"
func(s)
