import xlrd 
import xlwt 
import csv
from xlwt import Workbook 
wb=xlrd.open_workbook("NETWORK_LLD.xlsx") 
sheet=wb.sheet_by_index(1) 
sheet.cell_value(0,0) 
wbs=xlrd.open_workbook("INFRA_LLD.xlsx") 
sheets=wbs.sheet_by_index(0) 
sheets.cell_value(0,0) 
wbss=Workbook() 
sheet1=wbss.add_sheet('sheet 1') 
f=open("excelpython.txt","w") 
value=[] 
value1=[] 
value2=[] 
value3=[] 
val=[]
for x in range(sheet.ncols): 
	if sheet.cell_value(0,x) == "From Vendor": 
		k=x 
		for p in range(sheet.ncols): 
			if sheet.cell_value(0,p) == "Port": 
				l=p 
				for b in range(sheet.ncols): 
					if sheet.cell_value(0,b) == "From IP": 
						c=b 
						for d in range(sheet.ncols): 
							if sheet.cell_value(0,d) == "To IP": 
								e=d 
								for y in range(sheet.nrows): 
									if sheet.cell_value(y,k) == "SeaChange": 
										z=y 
										for column in range(sheets.ncols): 
          										if sheets.cell_value(1,column) == "Hostname": 
            											col=column 
             											for columns in range(sheets.ncols): 
               												if sheets.cell_value(1,columns) == "Prod_tenant IP Address": 
                												co=columns 
                												for row in range(sheets.nrows): 
                													if sheet.cell_value(z,c) == sheets.cell_value(row,co): 
                  														for rows in range(sheets.nrows): 
                   															if sheet.cell_value(z,e) == sheets.cell_value(rows,co):        
                    																port=sheet.cell_value(z,l) 
                   																if ',' in str(port): 
                     																	type=port.split(",") 
                     																	try: 
                      																		for lines in type: 
                       																			o=type[0] 
                       																			if '-' in str(o): 
                        																			type1=o.split("-") 
                        																			for step in type1: 
                         																				o1=type1[0] 
                         																				o2=type1[1] 
                         																				start=int(o1) 
                         																				end= int(o2) 
 																							val.append(sheets.cell_value(rows,col)) 
                        																				val.append(sheet.cell_value(z,e)) 
                        																				val.append(o1) 
                         																				val.append(sheets.cell_value(row,col)) 
                        																				value1.append(o1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                      																					value2.append(sheets.cell_value(rows,col)) 

                         																				sub=int(o2)-int(o1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                 	       																				for x in range(i): 
                          																					start=start+j 
																								val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                         																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                	       																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                        																					val.append(o2) 
                         																					val.append(sheets.cell_value(row,col)) 
                        																					value1.append(o2) 
                        																					value3.append(sheet.cell_value(z,e))
                         																					value.append(sheets.cell_value(row,col)) 
                        																					value2.append(sheets.cell_value(rows,col))
																					else :
 																						val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(o) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(o) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 
	

                       																			n=type[1]  
                       																			if '-' in str(n): 
                        																			type2=n.split("-") 
                        																			for step in type2: 
                         																				n1=type2[0] 
                         																				n2=type2[1]  
                 	       																				start=int(n1) 
                         																				end=int(n2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(n1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(n1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                        																				value.append(sheets.cell_value(row,col)) 
                        																				value2.append(sheets.cell_value(rows,col)) 
																							sub=int(n2)-int(n1) 
																				                        if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                         																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					start=start+j 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(n2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(n2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
                       																						break 


                         																			 
                       																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(n) 
                        																			val.append(sheets.cell_value(row,col)) 
                       																				value1.append(n) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 

                       																			q=type[2] 
                       																			if '-' in str(q): 
                        																			type3=q.split("-") 
                        																			for step in type3: 
                         																				q1=type3[0] 
                         																				q2=type3[1] 
                         																				start=int(q1) 
                         																				end= int(q2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(q1) 
                        																				val.append(sheets.cell_value(row,col)) 
                        																				value1.append(q1) 
                        																				value3.append(sheet.cell_value(z,e)) 
                        																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 

                         																				sub=int(q2)-int(q1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					start=start+j 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(q2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(q2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                         																					break 
                       																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(q) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(q) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 
 
                       																			r=type[3] 
                       																			if '-' in str(r): 
                        																			type4=r.split("-") 
                        																			for step in type4: 
                         																				r1=type4[0] 
                         																				r2=type4[1] 
                         																				start=int(r1) 
                         																				end= int(r2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(r1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(r1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 

                         																				sub=int(r2)-int(r1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                         																			for x in range(i): 
                          																					start=start+j 
                         																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(r2) 
                         																					val.append(sheets.cell_value(row,col)) 
                        																					value1.append(r2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                        																					break 
                      																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(r) 
                       																				val.append(sheets.cell_value(row,col)) 
                        																			value1.append(r) 
                       																				value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 

                      																			s=type[4] 
                      																			if '-' in str(s): 
                       																				type5=s.split("-") 
                        																			for step in type5: 
                        																				s1=type5[0] 
                       																					s2=type5[1] 
                         																				start=int(s1) 
                         																				end= int(s2) 
                       																					val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                       																					val.append(s1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(s1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 
 
                        																				sub=int(s2)-int(s1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                        																				if sub == 3000: 
                         																					i=2 
                         																					j=1000 
                        																				if sub == 100: 
                         																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					start=start+j 
                         																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(s2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(s2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                        																					break 
                      																			else: 
                       																				val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(s) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(s) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 
 
                      																			t=type[5] 
                      																			if '-' in str(t): 
                        																			type6=t.split("-") 
                        																			for step in type6: 
                        																				t1=type6[0] 
                        																				t2=type6[1] 
                         																				start=int(t1) 
                         																				end= int(t2) 
                        																				val.append(sheets.cell_value(rows,col)) 
                        																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(t1) 
                         																				val.append(sheets.cell_value(row,col)) 
                        																				value1.append(t1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 
 
                        																				sub=int(t2)-int(t1) 
                        																				if sub == 2: 
                         																					i=1 
                         																					j=1 
                         																				if sub == 3000: 
                         																					i=2 
                          																					j=1000 
                        																				if sub == 100: 
                         																					i=9 
                         																					j=10 
                       																					for x in range(i): 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(t2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(t2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                        																					value2.append(sheets.cell_value(rows,col)) 
 
                         																					break 
                       																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(t) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(t) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                      																				value2.append(sheets.cell_value(rows,col)) 
 
                       																			u=type[6] 
                       																			if '-' in str(u): 
                        																			type7=u.split("-") 
                        																			for step in type7: 
                         																				u1=type7[0] 
                         																				u2=type7[1] 
                         																				start=int(u1) 
                         																				end= int(u2)
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(u1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(u1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 

                         																				sub=int(u2)-int(u1) 
                         																				if sub == 2: 
                         																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					start=start+j 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                         																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(u2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(u2) 	
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 

                         																					break 
                      																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(u) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(u) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 
 
                       																			v=type[7] 
                       																			if '-' in str(v): 
                        																			type8=v.split("-") 
                        																			for step in type8: 
                         																				v1=type8[0] 
                        																				v2=type8[1] 
                         																				start=int(v1) 
                         																				end= int(v2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(v1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(v1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 
 
                         																				sub=int(v2)-int(v1) 
                         																				if sub == 2: 
                         																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(v2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(v2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                         																					break 
                       																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(v) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(v) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 
 
                       																			w=type[8] 
                       																			if '-' in str(w): 
                        																			type1=w.split("-") 
                        																			for step in type1: 
                         																				w1=type1[0] 
                         																				w2=type1[1] 
                         																				start=int(w1) 
                         																				end= int(w2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(w1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(w1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                        																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 
 
                         																				sub=int(w2)-int(w1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                          																					i=2 
                          																					j=1000 
                         																				if sub == 100: 
                          																					i=9 
                          																					j=10 
                         																				for x in range(i): 
                          																					start=start+j 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(w2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(w2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                        																					break 
                       																			else: 
                        																			val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(w) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append("Port:'"+w+"'") 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 

                       																			g=type[9] 
                       																			if '-' in str(g): 
                        																			type9=g.split("-") 
                        																			for step in type9: 
                         																				g1=type9[0] 
                         																				g2=type9[1] 
                         																				start=int(g1) 
                         																				end= int(g2) 
                         																				val.append(sheets.cell_value(rows,col)) 
                         																				val.append(sheet.cell_value(z,e)) 
                         																				val.append(g1) 
                         																				val.append(sheets.cell_value(row,col)) 
                         																				value1.append(g1) 
                         																				value3.append(sheet.cell_value(z,e)) 
                         																				value.append(sheets.cell_value(row,col)) 
                         																				value2.append(sheets.cell_value(rows,col)) 

                         																				sub=int(g2)-int(g1) 
                         																				if sub == 2: 
                          																					i=1 
                          																					j=1 
                         																				if sub == 3000: 
                         																					i=2 
                          																					j=1000 
                        																				if sub == 100: 
                         																					i=9 
                         																					j=10 
                       																					for x in range(i): 
                          																					start=start+j 
                        																					start=start+j 
                          																					val.append(sheets.cell_value(rows,col)) 
                          																					val.append(sheet.cell_value(z,e)) 
                          																					val.append(start) 
                          																					val.append(sheets.cell_value(row,col)) 
                          																					value1.append(start) 
                          																					value3.append(sheet.cell_value(z,e)) 
                          																					value.append(sheets.cell_value(row,col)) 
                          																					value2.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheets.cell_value(rows,col)) 
                         																					val.append(sheet.cell_value(z,e)) 
                         																					val.append(g2) 
                         																					val.append(sheets.cell_value(row,col)) 
                         																					value1.append(g2) 
                         																					value3.append(sheet.cell_value(z,e)) 
                         																					value.append(sheets.cell_value(row,col)) 
                         																					value2.append(sheets.cell_value(rows,col)) 
 
                        																					break 
                       																			else: 
                       																				val.append(sheets.cell_value(rows,col)) 
                        																			val.append(sheet.cell_value(z,e)) 
                        																			val.append(g) 
                        																			val.append(sheets.cell_value(row,col)) 
                        																			value1.append(g) 
                        																			value3.append(sheet.cell_value(z,e)) 
                        																			value.append(sheets.cell_value(row,col)) 
                        																			value2.append(sheets.cell_value(rows,col)) 

                    																	except IndexError: 
                    																		pass 
                   																	else: 
                    																		val.append(port) 
                    																		val.append(sheet.cell_value(z,e)) 
																				val.append(sheets.cell_value(row,col)) 
                   																		val.append(sheets.cell_value(rows,col)) 
                    																		value1.append(port) 
                    																		value3.append(sheet.cell_value(z,e)) 
																				value.append(sheets.cell_value(row,col)) 
                   																		value2.append(sheets.cell_value(rows,col)) 
list_length1=len(value1) 
lis_len=len(value) 
list_len=len(value2) 
for s in range(lis_len): 
	sheet1.write(s,3,value[s]) 
	sheet1.write(s,0,value2[s]) 
	sheet1.write(s,1,value3[s])   
for x in range(list_length1): 
 	sheet1.write(x,2,value1[x]) 
wbss.save('data.xlsx') 
f.close() 


myfile = xlrd.open_workbook('find.xlsx')
mysheet = myfile.sheet_by_index(0)
myCsvfile = open('data.csv', 'wb')
wr = csv.writer(myCsvfile, delimiter="\t")
for rownum in xrange(mysheet.nrows):
	wr.writerow(mysheet.row_values(rownum))
myCsvfile.close()

f=open("data.txt","w")
count = 0 
for var in val: 
	if (count == 0): 
		f.write("Dest_Host:"+str(var)+",") 
		count +=1 
	elif (count == 1): 
		f.write("Dest_prod_IP:"+str(var)+",") 
		count +=1 
	elif (count == 2): 
		f.write("Port:'"+str(var)+"',") 
		count +=1 
	elif (count == 3): 
		f.write("Source_Host:"+str(var)) 
		count +=1 
	elif (count == 4): 
		f.write("\n") 
		count = 0 
f.close() 


