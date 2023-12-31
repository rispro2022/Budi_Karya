import db.db_handler as database
from flask import request,make_response,jsonify
import datetime

def ShowBoxChoosedByToolStock(toolstock):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.toolTypeCode FROM eqp_d_toolstock a WHERE a.id = '"+toolstock+"'"
    cursor.execute(query)
    data = cursor.fetchone()
    tooltype = data[0]

    #query untuk mencari stasiunkerja berdasarkan tooltypecode
    query = "SELECT stasiunKerja FROM cpl_kirimtool02 WHERE toolTypeCode = '"+tooltype+"'"
    cursor.execute(query)
    data = cursor.fetchone()
    pilihanws = data[0]

    query = "SELECT b.id,b.nama,a.stasiunKerja FROM eqp_d_boxonws a JOIN eqp_r_toolbox b ON b.id = a.boxId WHERE a.stasiunKerja = 'wsgd' UNION SELECT b.id,b.nama,a.stasiunKerja FROM eqp_d_boxonws a JOIN eqp_r_toolbox b ON b.id = a.boxId WHERE a.stasiunKerja = '"+pilihanws+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)

def ShowWorkstationByToolBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT b.id AS 'idWS', b.nama AS 'namaWS' FROM eqp_d_boxonws a JOIN gen_r_stasiunkerja b ON b.id = a.stasiunKerja WHERE a.boxId = '"+idbox+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def ShowBoxByWorkstationPeminjaman(workstation):
    conn = database.connector()
    cursor = conn.cursor()

    tanggal = request.args.get("tanggal")
    now = datetime.datetime.now()
    now = str(now)
    query =   "SELECT*FROM \
    (SELECT DISTINCT  a.id, a.toolTypeCode, e.nama, b.boxId, c.stasiunKerja AS SKtool, \
    d.stasiunKerja AS SKBox, a.quantity, \
    case \
	when d.stasiunKerja IS NOT NULL then d.stasiunKerja \
	when c.stasiunKerja IS NOT NULL then c.stasiunKerja \
    END onWs, f.tanggal FROM eqp_d_toolstock a \
    LEFT JOIN eqp_d_boxitem b ON a.id = b.toolStockId \
    LEFT JOIN eqp_d_toolonws c ON a.id = c.toolStockId \
    LEFT JOIN eqp_d_boxonws d ON b.boxId = d.boxId \
    LEFT JOIN eqp_r_tooltype e ON e.codes=a.toolTypeCode \
    LEFT JOIN cpl_kirimtool02 f on e.codes=f.toolTypeCode \
    WHERE c.logout IS NULL AND b.endDate IS NULL)CC1 WHERE CC1.onWs='"+workstation+"' AND CC1.tanggal = '"+tanggal+"'\
    AND CC1.id NOT IN (SELECT toolId FROM eqp_d_toolpinjam) "

    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def PeminjamanPerkakasByWorkstation(workstation,tanggal):
    conn = database.connector()
    cursor = conn.cursor()

    query_insert = "INSERT INTO eqp_d_toolpinjam(boxId,toolId,operatorId,tanggalPinjam)VALUES(%s,%s,%s,%s)"
    now = datetime.datetime.now()
    try:
        data = request.json
        uuidoperator = data["uuid"]

        query =   "SELECT * FROM \
        (SELECT DISTINCT  a. id, a.toolTypeCode, e.nama, b.boxId, c.stasiunKerja AS SKtool, \
        d.stasiunKerja AS SKBox, a.quantity, \
        case \
	    when d.stasiunKerja IS NOT NULL then d.stasiunKerja \
	    when c.stasiunKerja IS NOT NULL then c.stasiunKerja \
        END onWs, f.tanggal FROM eqp_d_toolstock a \
        LEFT JOIN eqp_d_boxitem b ON a.id = b.toolStockId \
        LEFT JOIN eqp_d_toolonws c ON a.id = c.toolStockId \
        LEFT JOIN eqp_d_boxonws d ON b.boxId = d.boxId \
        LEFT JOIN eqp_r_tooltype e ON e.codes=a.toolTypeCode \
        LEFT JOIN cpl_kirimtool02 f on e.codes=f.toolTypeCode \
        WHERE c.logout IS NULL AND b.endDate IS NULL)CC1 WHERE CC1.onWs='"+workstation+"' AND CC1.tanggal = '"+tanggal+"'"
        cursor.execute(query)
        records = cursor.fetchall()
        
      
        query_operator = "SELECT a.operatorid FROM opr_d_dictoperator a WHERE a.uuid = '"+uuidoperator+"'"
        cursor.execute(query_operator)
        data = cursor.fetchone()

        idoperator = data[0]
        for index in records:
            idbox = index[3]
            idtool = index[0]
            print("idtool : ",idtool)
            values = (idbox,idtool,idoperator,now)
            cursor.execute(query_insert,values)
        
        print("operator : ",idoperator)
        conn.commit()
        hasil = {"status" : "berhasil"}

    except Exception as e:
        hasil = {"status" : "gagal"}
        print("error",str(e))
    return hasil
    



def ShowWorkstationToolsByToolBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT b.id,b.nama,c.toolStockId FROM eqp_d_boxonws a JOIN gen_r_stasiunkerja b on b.id = a.stasiunKerja JOIN eqp_d_toolonws c on c.stasiunKerja = b.id WHERE a.boxId = '"+idbox+"'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)


def PengemasanToolStockToBox(toolstock,idbox):
    conn =  database.connector()
    cursor = conn.cursor()
    query = "INSERT INTO eqp_d_boxitem(toolStockId,boxId,startDate)VALUES(%s,%s,%s)"
    
    try:    
        startdate = datetime.datetime.now()
        values = (toolstock,idbox,startdate)
        cursor.execute(query,values)
        query = "DELETE FROM eqp_d_boxonws WHERE boxid = '"+idbox+"' AND stasiunKerja = 'WSGD'"
        cursor.execute(query)
        query_select = "SELECT a.toolTypeCode, a.quantity, a.unit,b.multiplier  FROM eqp_d_toolstock a JOIN eqp_r_tooltype c on c.codes = a.toolTypeCode JOIN gen_r_materialunit b on b.id = a.unit WHERE a.id = '"+toolstock+"'"
        cursor.execute(query_select)
        records = cursor.fetchone()

        tooltype = records[0]
        qty = int(records[1])
        multiplier = int(records[3])

        qty_total = qty * multiplier

        query_select2 = "SELECT kurangPengemasan FROM cpl_kirimtool02 WHERE toolTypeCode = '"+tooltype+"'"
        cursor.execute(query_select2)
        data2 = cursor.fetchone()
        qty_pengemasan = int(data2[0])

        qty_akhir = qty_pengemasan - qty_total

        if qty_akhir <= 0:
            qty_akhir = 0

        query_update = "UPDATE cpl_kirimtool02 SET kurangPengemasan = %s WHERE toolTypeCode = %s"
        values2 = (qty_akhir,tooltype)
        cursor.execute(query_update,values2)
        
        conn.commit()
        hasil = {"status" : "berhasil"}
    except Exception as e:
        print("error",str(e))
        hasil = {"status" : "gagal"}
    return hasil


def ShowInsertedToolStockInBox(idbox):
    conn = database.connector()
    cursor = conn.cursor()
    query = "SELECT a.boxId,a.toolStockId,c.nama AS 'namaTool' FROM eqp_d_boxitem a JOIN eqp_d_toolstock b ON b.id = a.toolStockId JOIN eqp_r_tooltype c ON c.codes = b.toolTypeCode WHERE a.boxId = '"+idbox+"' AND startDate != '0000-00-00 00:00:00'"
    cursor.execute(query)
    records = cursor.fetchall()
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    
    for data in records:
        json_data.append(dict(zip(row_headers,data)))
    
    return  make_response(jsonify(json_data),200)