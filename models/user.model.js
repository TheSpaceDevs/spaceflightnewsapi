const mongoose = require('mongoose');
const mongoosePaginate = require('mongoose-paginate-v2');
const uniqueValidator = require('mongoose-unique-validator');
const bcrypt = require('bcryptjs');

const { Schema } = mongoose;
const SALT_WORK_FACTOR = 10;

const userSchema = new Schema({
  firstname: {
    type: String,
    required: true,
  },
  lastname: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true,
    select: false
  },
  roles: {
    type: [String],
    required: true,
    default: ['user']
  }
});

userSchema.plugin(mongoosePaginate);
userSchema.plugin(uniqueValidator);

userSchema.pre('save', async function save(next) {
  try {
    const salt = await bcrypt.genSalt(SALT_WORK_FACTOR);
    this.password = await bcrypt.hash(this.password, salt);
    return next();
  } catch (err) {
    return next(err);
  }
});

const UserModel = mongoose.model('Users', userSchema);

module.exports = UserModel;