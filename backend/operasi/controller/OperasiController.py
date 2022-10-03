from numpy import record
import db.db_handler as database
from flask import request,make_response,jsonify
import random
import string
from product.controller.ProdukController import *
import datetime

def ShowOperasiFromProduct(idProduct):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'idOperasi',a.rencanaMulai,a.rencanaSelesai, b.id AS 'idProses',b.nama AS 'namaProses',a.produk, i.operatorid,j.nama AS 'namaOperator' ,k.keterangan AS 'keteranganWS' FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN opr_d_operatorneed i ON i.operationid = a.id JOIN opd_r_operator j ON j.code = i.operatorid JOIN gen_r_stasiunkerja k ON k.id = a.stasiunKerja WHERE h.id = '"+idProduct+"' ORDER BY a.rencanaMulai ASC"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)


def ShowProductInOperasi(id_product):
    conn = database.connector()
    cursor = conn.cursor()
    rencana_mulai_min = ""

    query_min = "SELECT MIN(a.SCHEDULLEDSTARTOPERATION) FROM prd_d_operation a"
    cursor.execute(query_min)
    records = cursor.fetchall()
    for data in records:
        rencana_mulai_min = data[0]
        rencana_mulai_min = str(rencana_mulai_min)
    print(rencana_mulai_min)

    #query = "SELECT a.id,a.rencanaMulai, b.id AS 'idProduk',b.dueDate AS 'dueDateProduk', c.id AS 'idRincian',c.jumlah,c.dueDate AS 'dueDateRincian', d.id AS 'idProyek', d.nama AS 'namaProyek', e.id AS 'idCustomer', e.nama AS 'namaCustomer' FROM prd_d_operasi a JOIN prd_d_produk b ON b.id = a.produk JOIN prd_r_rincianproyek c ON c.id = b.rincianProyek JOIN prd_r_proyek d ON d.id = c.proyek JOIN gen_r_customer e ON e.id = d.customerid WHERE a.produk = '"+id_product+"' AND a.rencanaMulai = '"+rencana_mulai_min+"'"
    query = "SELECT a.ID AS 'idOperasi',a.SCHEDULLEDSTARTOPERATION,a.SCHEDULLEDFINISHOPERATION, b.id AS 'idProses',b.nama AS 'namaProses',a.produk, i.operatorid,j.nama AS 'namaOperator' FROM prd_d_operation a JOIN prd_r_process b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN opr_d_operatorneed i ON i.operationid = a.id JOIN opd_r_operator j ON j.code = i.operatorid WHERE h.id = '"+id_product+"' ORDER BY a.proses,a.rencanaMulai ASC"
    cursor.execute(query)
    records_query = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records_query:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def PantauOperasi(idProduct):
    conn = database.connector()
    cursor = conn.cursor()

    query = "SELECT a.id AS 'idOperasi',a.rencanaMulai,a.rencanaSelesai, b.id AS 'idProses',b.nama AS 'namaProses',a.produk, i.operatorid,j.nama AS 'namaOperator' FROM prd_d_operasi a JOIN prd_r_proses b ON b.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = b.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN opr_d_operatorneed i ON i.operationid = a.id JOIN opd_r_operator j ON j.code = i.operatorid WHERE h.id = '"+idProduct+"' ORDER BY a.rencanaMulai ASC"
    cursor.execute(query)

    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)

def GetProcessofProduct(idProduk):
    conn = database.connector()
    cursor = conn.cursor()
    query2 = "SELECT a.id FROM prd_r_proses a JOIN prd_r_strukturjnsprd b ON b.idNodal = a.nodalOutput JOIN prd_r_jenisproduk c ON c.id = b.jnsProduk JOIN prd_r_rincianproyek d ON d.jenisProduk = c.id JOIN prd_r_proyek e ON e.id = d.proyek JOIN prd_d_produk f ON f.rincianProyek = d.id WHERE f.id = '"+idProduk+"'"
    cursor.execute(query2)
    records = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))    
    
    return make_response(jsonify(json_data),200)




def fetchProcesstoOperation(idProduk):
    conn = database.connector()
    cursor = conn.cursor()
    query3 = "SELECT c.id AS 'IdProses',a.stasiunKerja,c.durasi,i.qualificationCode FROM gen_r_mampuproses a JOIN prd_r_proses c ON c.id = a.proses JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id JOIN prd_r_proyek g ON g.id = f.proyek JOIN prd_d_produk h ON h.rincianProyek = f.id JOIN prd_r_operatorrequirement i ON i.processCode = c.id WHERE h.id = '"+idProduk+"'ORDER BY c.id DESC"
    #query3 = "SELECT c.id AS 'IdProses',a.stasiunKerja,c.durasi,i.qualificationCode"
    #query3 = query3  +   "FROM gen_r_mampuproses a "
    #query3 = query3  +   "JOIN prd_r_proses c ON c.id = a.proses"
    #query3 = query3  +   "JOIN prd_r_strukturjnsprd d ON d.idNodal = c.nodalOutput"
    #query3 = query3  +   "JOIN prd_r_jenisproduk e ON e.id = d.jnsProduk"
    #query3 = query3  +   "JOIN prd_r_rincianproyek f ON f.jenisProduk = e.id"
    #query3 = query3  +   "JOIN prd_r_proyek g ON g.id = f.proyek"
    #query3 = query3  +   "JOIN prd_d_produk h ON h.rincianProyek = f.id"         
    ##query3 = query3  +   "JOIN prd_r_operatorrequirement i ON i.processCode = c.id"
    #query3 = query3 +    "WHERE h.id = '"+idProduk+"' ORDER BY c.id DESC"

    cursor.execute(query3)
    recordsFetch = cursor.fetchall()
    return recordsFetch


def fetchDateProyektoOperation(idProduk):
    conn = database.connector()
    cursor = conn.cursor()
    query5 = "SELECT a.tglDibuat FROM prd_r_proyek a JOIN prd_r_rincianproyek b ON b.proyek = a.id JOIN prd_d_produk c ON c.rincianProyek = b.id WHERE c.id = '"+idProduk+"'"
    #query5 = "SELECT a.tglDibuat FROM prd_r_proyek a"
    #query5 = query5 + "JOIN prd_r_rincianproyek b ON b.proyek = a.id"
    #query5 = query5 + "JOIN prd_d_produk c ON c.rincianProyek = b.id"
    #query5 = query5 + "WHERE c.id = '"+idProduk+"'"
    cursor.execute(query5)
    recorddate = cursor.fetchall()
    return recorddate



def fetchOperatorQualification():
    conn = database.connector()
    cursor = conn.cursor()
    query7 = "SELECT a.operatorid,a.qualificationCode,b.descriptions FROM opr_d_operatorlevel a JOIN opr_r_operatorqualification b ON b.codes = a.qualificationCode"
    #query7 = "SELECT a.operatorid,a.qualificationCode,b.descriptions"
    ##query7 = query7 + "FROM opr_d_operatorlevel a"
    #query7 = query7 + "JOIN opr_r_operatorqualification b ON b.codes = a.qualificationCode"
    cursor.execute(query7)
    recordsqualification = cursor.fetchall()
    return recordsqualification


def fetchRequirementsCode(idProduk):
    datafetch = []
    requirementsCode = ''
    datafetch = fetchProcesstoOperation(idProduk)
    for index in datafetch:
        requirementsCode = index[3]
    return requirementsCode


def fetchSchedulledStart(idProduk):
    recordDate = []
    schedulledstartWorkDate = ""
    recordDate = fetchDateProyektoOperation(idProduk)
    for data in recordDate:
        schedulledstartWorkDate = data[0]
    return schedulledstartWorkDate


def fetchSchedulledFinish(idProduk):
    recordDate = []
    scehdulledFinishWorkDate = ""
    recordDate = fetchDateProyektoOperation(idProduk)
    for data in recordDate:
       scehdulledFinishWorkDate = data[0]
    return scehdulledFinishWorkDate

    

def GenerateOperation(idProduk):
    conn = database.connector()
    cursor = conn.cursor()
    
    N = 9
    counter=1
    print("ID Product : ",idProduk)
    proses = ""   
    stasiunKerja = ""
    recordsFetch = []
    records_oprqualification = []

    query = "INSERT INTO prd_d_operasi(id,rencanaMulai,rencanaSelesai,proses,stasiunKerja,produk)VALUES(%s,%s,%s,%s,%s,%s)"
    query_insert_operatorneed = "INSERT INTO opr_d_operatorneed(operationid,operatorid)VALUES(%s,%s)"     
    try:
       
       
        recordsFetch = fetchProcesstoOperation(idProduk)
        records_oprqualification = fetchOperatorQualification()
        schedulledstartWorkDate = fetchSchedulledStart(idProduk)
        schedulledFinishWorkDate = fetchSchedulledFinish(idProduk)
       
        print(recordsFetch)
       #Requirement Code => punya proses
       #Qualification => punya operator

        for index in recordsFetch:
            id_operation = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            proses = index[0]
            stasiunKerja = index[1]
            durasi = index[2]
            requirementsCode = index[3]
            cek = False 
            while cek == False:
                if counter % 2 != 0 and cek == False:
                    schedulledFinishWorkDate = schedulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    values1 = (id_operation,schedulledstartWorkDate,schedulledFinishWorkDate,proses,stasiunKerja,idProduk)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = schedulledFinishWorkDate
                    for index2 in records_oprqualification:
                        operatorid = index2[0]
                        qualificationCode = index2[1]
                        if qualificationCode == requirementsCode:
                            values_oprneed = (id_operation,operatorid)
                            cursor.execute(query_insert_operatorneed,values_oprneed)
                   
                    cek = True
                elif counter %2 == 0 and cek == False:
                    schedulledFinishWorkDate = schedulledFinishWorkDate + datetime.timedelta(minutes = durasi)
                    cursor.execute(query,values1)
                    schedulledstartWorkDate = schedulledFinishWorkDate
                    for index2 in records_oprqualification:
                        operatorid = index2[0]
                        qualificationCode = index2[1]
                        if qualificationCode == requirementsCode:
                            values_oprneed = (id_operation,operatorid)
                            cursor.execute(query_insert_operatorneed,values_oprneed)
                    cek = True
        counter = counter + 1
        #conn.commit()
        hasil = {"status" : "berhasil"}
        print(hasil)
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowProductInPantauOperasi():
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.id , b.id AS 'IdRincian', b.jumlah, c.nama AS 'NamaProyek', d.nama AS 'NamaCustomer' FROM prd_d_produk a JOIN prd_r_rincianproyek b ON a.rincianProyek = b.id JOIN prd_r_proyek c ON c.id = b.proyek JOIN gen_r_customer d ON d.id = c.customerid"
    cursor.execute(query)
    records = cursor.fetchall()

    json_data = []
    row_headers = [x[0] for x in cursor.description]

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    return make_response(jsonify(json_data),200)




def StartOperation(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()
    dates = ''
    dates = datetime.datetime.now()
    query = "UPDATE prd_d_operasi SET mulai = %s WHERE id = %s"
    values = (dates,idOperasi)
    cursor.execute(query,values)
    conn.commit()
    hasil = {"status" : "berhasil"}
    return hasil


def EndOperation(idOperasi):
    conn = database.connector()
    cursor = conn.cursor()

    #update kolom selesai
    dates = ''
    dates = datetime.datetime.now()
    query = "UPDATE prd_d_operasi SET selesai = %s WHERE id = %s"
    values = (dates,idOperasi)
    cursor.execute(query,values)

    #status menjadi 1 atau selesai
    query2 = "UPDATE prd_d_operasi SET status = %s WHERE id = %s"
    values2 = (1,idOperasi)
    cursor.execute(query2,values2)
    conn.commit()
    hasil = {"status" : "berhasil"}
    return hasil