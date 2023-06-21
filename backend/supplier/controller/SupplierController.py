import db.db_handler as db
from flask import request,make_response,jsonify

def AddSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "INSERT INTO gen_r_supplier(code,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        data = request.json
        code = data["code"]
        nama = data["nama"]
        adress1 = data["adress1"]
        adress2 = data["adress2"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        fax = data["fax"]
        email = data["email"]
        situs = data["situs"]
        pic = data["pic"]
        remark = data["remark"]
        city = data["city"]
        values = (code,nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def UpdateSupplier(code):
    conn = db.connector()
    cursor = conn.cursor()

    query = "UPDATE gen_r_supplier SET nama = %s,adress1 = %s,adress2 = %s,postalcode = %s,phone = %s,fax = %s,email = %s,situs = %s,pic = %s,remark = %s,city = %s WHERE code = '"+code+"'"
    try:
        data = request.json
        nama = data["nama"]
        adress1 = data["adress1"]
        adress2 = data["adress2"]
        postalcode = data["postalcode"]
        phone = data["phone"]
        fax = data["fax"]
        email = data["email"]
        situs = data["situs"]
        pic = data["pic"]
        remark = data["remark"]
        city = data["city"]
        values = (nama,adress1,adress2,postalcode,phone,fax,email,situs,pic,remark,city)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil

def GetSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT * FROM gen_r_supplier"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def GetSupplierById(idSupplier):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT b.code,b.nama,b.adress1 FROM gen_r_supplierrangking a JOIN gen_r_supplier b ON b.code = a.IDSupplier WHERE a.IDSupplier = '"+idSupplier+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)





def RankingSupplier():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.IDSupplier,b.nama AS 'namaSupplier',a.Rangking,a.Bobot FROM gen_r_supplierrangking a JOIN gen_r_supplier b ON b.code = a.IDSupplier"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def GetDetailRankingSupplier(idSupplier):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT Z0.materialTypeCode,C.nama, Z0.supplierCode, Z1.Harga, Z1.Satuan, \
    Z0.LeadTime, Z0.satuan, Z2.MinimalOrder, Z2.Satuan FROM \
    (SELECT A.materialTypeCode, A.supplierCode, A.Nilai LeadTime, A.Satuan \
    FROM mat_r_materialtypesupplier A \
    WHERE idKriteria = 'K03')Z0\
    LEFT JOIN \
    (SELECT A.materialTypeCode, A.supplierCode,  A.Nilai Harga, A.Satuan \
    FROM mat_r_materialtypesupplier A \
    WHERE idKriteria = 'K02')Z1 ON Z0.materialTypeCode=Z1.materialTypeCode \
    LEFT JOIN \
    (SELECT A.materialTypeCode,A.supplierCode, A.Nilai MinimalOrder, A.Satuan \
    FROM mat_r_materialtypesupplier A WHERE A.IDKriteria = 'K05')Z2 ON Z2.materialTypeCode = Z1.materialTypeCode\
    JOIN mat_r_materialtype C ON Z1.materialTypeCode=C.code WHERE Z0.supplierCode= '"+idSupplier+"'"

    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def GetPeringkatKriteria():
    conn = db.connector()
    cursor = conn.cursor()

    query = "SELECT a.IDKriteria,b.namaKriteria,a.rangking,a.Bobot FROM gen_r_kriteriabobot a JOIN gen_r_kriteria b ON b.ID = a.IDKriteria ORDER BY a.Bobot DESC"
    cursor.execute(query)
    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)



def GetKriteriaPemasok():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.ID AS 'IdKriteria',a.namaKriteria,a.mulai,a.selesai FROM gen_r_kriteria a"

    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)



def InsertMatriksKriteria():
    conn = db.connector()
    cursor = conn.cursor()
    query = "INSERT INTO gen_r_matrikskriteria(IDKriteria,IDKriteria02,Nilai)VALUES(%s,%s,%s)"
    try:
        data = request.json
        IDKriteria = data["criteria01"]
        IDKriteria02 = data["criteria02"]
        nilai = data["Nilai"]
        values = (IDKriteria,IDKriteria02,nilai)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def InsertMatriksKriteriaByAdmin(idPenghitung):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT ID FROM gen_r_adminperhitungan WHERE ID = '"+idPenghitung+"'"
    cursor.execute(query)
    record = cursor.fetchone()
    idpenghitung = record[0]
    query_insert = "INSERT INTO gen_r_matrikskriteria(IDKriteria,IDKriteria02,Nilai,idPenghitung)VALUES(%s,%s,%s,%s)"

    try:
        data = request.json
        IDKriteria = data["criteria01"]
        IDKriteria02 = data["criteria02"]
        nilai = data["Nilai"]

        values = (IDKriteria,IDKriteria02,nilai,idpenghitung)
        cursor.execute(query_insert,values)
        conn.commit()

        hasil = {"status" : "berhasil"}


    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    
    return hasil
        




def GetMatriksKriteriaInput():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.IDKriteria,b.namaKriteria,a.IDKriteria02,c.namaKriteria AS 'namaKriteria02',a.nilai FROM gen_r_matrikskriteria a JOIN gen_r_kriteria b ON b.ID = a.IDKriteria JOIN gen_r_kriteria c ON c.ID = a.IDKriteria02 WHERE a.konfirm IS NULL"
    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)


def GetMatriksKriteriaInputByAdmin(IdPenghitung):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT b.IDKriteria AS 'IdKriteria01',c.namaKriteria AS 'namaKriteria01', "
    query += "b.IDKriteria02 AS 'IdKriteria02', d.namaKriteria AS 'namaKriteria02',b.Nilai " 
    query += "FROM gen_r_adminperhitungan a "
    query += "JOIN gen_r_matrikskriteria b ON b.idPenghitung = a.ID "
    query += "JOIN gen_r_kriteria c ON c.ID = b.IDKriteria "
    query += "JOIN gen_r_kriteria d ON d.ID = b.IDKriteria02 "
    query += "WHERE a.ID = '"+IdPenghitung+"' AND b.konfirm IS NULL"

    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)



def GetPerbandinganSupplierByAdmin(idPenghitung):
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT b.IDKriteria,b.IDSupplier01,b.IDSupplier02,b.nilai "
    query += "FROM gen_r_adminperhitungan a "
    query += "JOIN gen_r_perbandingan b ON b.idPenghitung = a.ID "
    query += "WHERE a.ID = '"+idPenghitung+"' AND b.konfirm IS NULL "

    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)




def InsertNewPenghitung():
    conn = db.connector()
    cursor = conn.cursor()
    query = "INSERT INTO gen_r_adminperhitungan(ID,namaPenghitung,tglPenghitung)VALUES(%s,%s,%s)"
    try:
        data = request.json
        idpenghitung = data["idPenghitung"]
        namapenghitung = data["namaPenghitung"]
        tglPenghitung = data["tglPenghitung"]
        values = (idpenghitung,namapenghitung,tglPenghitung)
        cursor.execute(query,values)
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("Error",str(e))
        hasil = {"status" : "gagal"}
    return hasil



def GetPenghitungMatriks():
    conn = db.connector()
    cursor = conn.cursor()
    query = "SELECT a.ID AS 'idPenghitung',a.namaPenghitung,a.tglPenghitung FROM gen_r_adminperhitungan a"
    cursor.execute(query)

    records = cursor.fetchall()
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []

    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return make_response(jsonify(json_data),200)








    
