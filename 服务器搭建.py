from flask import Flask, request, jsonify
import pymysql

# 创建 Flask 应用
app = Flask(__name__)

# 数据库配置
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1q2W3e,."
DB_NAME = "software_project"

# 数据库连接函数
def get_db_connection():
    return pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             password=DB_PASSWORD,
                             database=DB_NAME,
                             charset='utf8mb4')

# 查询操作示例
@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `user_id` = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            if result:
                return jsonify({"user_id": result[0], "user_name": result[1], "password":result[2]}), 200
            else:
                return jsonify({"message": "User not found"}), 404
    finally:
        connection.close()

# 插入操作示例
@app.route('/user', methods=['POST'])
def add_user():
    user_id = request.json.get('user_id')
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    tel = request.json.get('tel')
    score = request.json.get('score')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `user` (`user_id`,`user_name`, `password`, `tel`, `score`) VALUES (%s,%s, %s, %s, %s)"
            cursor.execute(sql, (user_id,user_name, password, tel, score))
            connection.commit()
            return jsonify({"message": "User added successfully"}), 201
    finally:
        connection.close()

# 删除操作示例
@app.route('/user', methods=['DELETE'])
def delete_user():
    user_id = request.json.get('user_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `user` WHERE `user_id` = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            return jsonify({"message": "User deleted successfully"}), 200
    finally:
        connection.close()

# 更新操作示例
@app.route('/user', methods=['PUT'])
def update_user():
    user_id = request.json.get('user_id')
    user_name = request.json.get('user_name')
    tel = request.json.get('tel')
    score = request.json.get('score')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `user` SET `user_name` = %s, `tel` = %s, `score` = %s WHERE `user_id` = %s"
            cursor.execute(sql, (user_name, tel, score, user_id))
            connection.commit()
            return jsonify({"message": "User updated successfully"}), 200
    finally:
        connection.close()
# 查询操作：GET 请求 - 查询需求
@app.route('/require', methods=['GET'])
def get_require():
    req_id = request.args.get('req_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `require` WHERE `req_id` = %s"
            cursor.execute(sql, (req_id,))
            result = cursor.fetchone()
            if result:
                return jsonify({"req_id": result[0], "req_time": result[1], "req_score": result[2], "from_user_id": result[3],
                                "req_situation": result[4], "to_user_id": result[5],"req_position":result[6],"need":result[7]}), 200
            else:
                return jsonify({"message": "Requirement not found"}), 404
    finally:
        connection.close()

# 插入操作：POST 请求 - 添加需求
@app.route('/require', methods=['POST'])
def add_require():
    req_time = request.json.get('req_time')
    req_score = request.json.get('req_score')
    from_user_id = request.json.get('from_user_id')
    req_situation = request.json.get('req_situation')
    to_user_id = request.json.get('to_user_id')
    req_position = request.json.get('req_position')
    need = request.json.get('need')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `require` (`req_time`, `req_score`,`from_user_id`, `req_situation`, `to_user_id`,`req_position`, `need`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (req_time, req_score,from_user_id, req_situation,to_user_id, req_position, need))
            connection.commit()
            return jsonify({"message": "Requirement added successfully"}), 201
    finally:
        connection.close()

# 删除操作：DELETE 请求 - 删除需求
@app.route('/require', methods=['DELETE'])
def delete_require():
    req_id = request.json.get('req_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `require` WHERE `req_id` = %s"
            cursor.execute(sql, (req_id,))
            connection.commit()
            return jsonify({"message": "Requirement deleted successfully"}), 200
    finally:
        connection.close()

# 更新操作：PUT 请求 - 更新需求
@app.route('/require', methods=['PUT'])
def update_require():
    req_id = request.json.get('req_id')
    need=request.json.get('need')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `require` SET `need` = %s WHERE `req_id` = %s"
            cursor.execute(sql, (need, req_id))
            connection.commit()
            return jsonify({"message": "Requirement updated successfully"}), 200
    finally:
        connection.close()
# 查询操作：GET 请求 - 查询用户需求
@app.route('/user_require', methods=['GET'])
def get_user_require():
    user_id = request.args.get('user_id')
    req_id = request.args.get('req_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user_require` WHERE `user_id` = %s AND `req_id` = %s"
            cursor.execute(sql, (user_id,req_id))
            result = cursor.fetchall()
            if result:
                return jsonify({"user_id": result[0], "req_id": result[1],"req_time": result[2], "r_or_h": result[3],"another_user_id": result[4]}), 200
            else:
                return jsonify({"message": "No requirements found for this user"}), 404
    finally:
        connection.close()

# 插入操作：POST 请求 - 添加用户需求
@app.route('/user_require', methods=['POST'])
def add_user_require():
    user_id = request.json.get('user_id')
    req_id = request.json.get('req_id')
    req_time = request.json.get('req_time')
    r_or_h = request.json.get('r_or_h')
    another_user_id = request.json.get('another_user_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `user_require` (`user_id`, `req_id`,`req_time`,`r_or_h`,`another_user_id`) VALUES (%s, %s,%s, %s,%s)"
            cursor.execute(sql, (user_id, req_id,req_time,r_or_h,another_user_id))
            connection.commit()
            return jsonify({"message": "User requirement added successfully"}), 201
    finally:
        connection.close()

# 删除操作：DELETE 请求 - 删除用户需求
@app.route('/user_require', methods=['DELETE'])
def delete_user_require():
    user_id = request.json.get('user_id')
    require_id = request.json.get('require_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `user_require` WHERE `user_id` = %s AND `require_id` = %s"
            cursor.execute(sql, (user_id, require_id))
            connection.commit()
            return jsonify({"message": "User requirement deleted successfully"}), 200
    finally:
        connection.close()
# 更新操作：PUT 请求 - 更新需求
@app.route('/user_require', methods=['PUT'])
def update_user_require():
    req_id = request.json.get('req_id')
    need=request.json.get('need')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `user_require` SET `need` = %s WHERE `req_id` = %s"
            cursor.execute(sql, (need, req_id))
            connection.commit()
            return jsonify({"message": "user_Requirement updated successfully"}), 200
    finally:
        connection.close()
# 查询操作：GET 请求 - 查询聊天记录
@app.route('/chat', methods=['GET'])
def get_chat():
    mess_ID = request.args.get('mess_ID')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `chat` WHERE `mess_ID` = %s"
            cursor.execute(sql, (mess_ID,))
            result = cursor.fetchone()
            if result:
                return jsonify({"mess_ID": result[0], "send_user_id": result[1], "rec_user_id": result[2], "send_time": result[3],"content":result[4]}), 200
            else:
                return jsonify({"message": "Chat not found"}), 404
    finally:
        connection.close()

# 插入操作：POST 请求 - 添加聊天记录
@app.route('/chat', methods=['POST'])
def add_chat():
    mess_ID = request.json.get('mess_ID')
    send_user_id = request.json.get('send_user_id')
    rec_user_id = request.json.get('rec_user_id')
    send_time = request.json.get('send_time')
    content = request.json.get('content')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `chat` (`mess_ID`, `send_user_id`,`rec_user_id`, `send_time`, `content`) VALUES (%s, %s, %s,%s,%s)"
            cursor.execute(sql, (mess_ID,send_user_id,rec_user_id, send_time, content))
            connection.commit()
            return jsonify({"message": "Chat message added successfully"}), 201
    finally:
        connection.close()

# 删除操作：DELETE 请求 - 删除聊天记录
@app.route('/chat', methods=['DELETE'])
def delete_chat():
    chat_id = request.json.get('chat_id')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `chat` WHERE `chat_id` = %s"
            cursor.execute(sql, (chat_id,))
            connection.commit()
            return jsonify({"message": "Chat message deleted successfully"}), 200
    finally:
        connection.close()


# 启动服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在所有接口监听5000端口
