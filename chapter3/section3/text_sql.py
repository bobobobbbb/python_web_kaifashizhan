rs = session.query(User).filter(
    text('id > 2 and id < 4').order_by(text('id')).all()
)
get_result(rs)
rs = session.query(User).filter(text('id < :value and name = :name')).params(
    values = 3, name = 'xiaoming'
).all()
get_result(rs)
rs = session.query(User).from_statment(
    text('SELECT * FROM users where name = :name')).params(name='wanglang').all()
get_result(rs)
