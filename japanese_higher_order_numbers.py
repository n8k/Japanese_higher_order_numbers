import math as m

def formatter(n):
	return_format = '0,.0f'
	if n in range(-100, 100):
		return_format = '0.1f'
	return format(n/10.0 ,return_format)

def num_to_jp(n, *args):

	jp_number_postfix = { 
	0:"",			# For n < 10,000 do not append　
	4:"万",			# For n > 10^4	 append 'man'
	8:"億", 			# For n > 10^8  append 'oku'
	12:"兆",			# For n > 10^12 append 'chou'
	16:"京",			# For n > 10^16 append 'kei'
	20:"垓",			# For n > 10^20 append 'gai'
	24:"𥝱",			# For n > 10^24 append 'jyo'
	28:"穣",			# For n > 10^28 append 'jyou'
	32:"溝",			# For n > 10^32 append 'kou'
	36:"澗",			# For n > 10^36 append 'kan'
	40:"正",			# For n > 10^40 append 'sei'
	44:"載",			# For n > 10^44 append 'sai'
	48:"極",			# For n > 10^48 append 'goku'
	52:"恒河沙",		# For n > 10^52 append 'gougasha'
	56:"阿僧祇",		# For n > 10^56 append 'asougi'
	60:"那由他",		# For n > 10^60 append 'nayuta'
	64:"不可思議"		# For n > 10^64 append 'fukashigi'
	}

	exponent = m.floor(m.log10(abs(n)))
	significand = n / 10**exponent
	decimal_places = exponent % 4
	
	print(significand, decimal_places)
	
	result_signifcand = str(formatter(significand * 10**(decimal_places+1)))
	result_postfix = str(jp_number_postfix.get(exponent - decimal_places, "Error"))
	
	if result_postfix == "Error":
		return "Error: Maximum output value is 9,999 x 10^64"

	if n in range(-9999,9999):
		result = formatter(n)
	else:
		result = result_signifcand + result_postfix
	if args:
		result += str(args[0])

	return result