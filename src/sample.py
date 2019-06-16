import tensorflow as tf

var = tf.Variable(0)
holder = tf.placeholder(tf.int32)
app_op = tf.add(var, holder)
update_var = tf.assign(var ,add_op)
mul_op = tf.mul(add_op, update_var)

with tf.Session() as session:
    summary_writer = tf.train.SummaryWriter('/var/log', graph = session.graph)
    session.run(tf.initialize_all_variables())

    result = session.run(mul_op, feed_dict={ holder: 5})

    print(result)
