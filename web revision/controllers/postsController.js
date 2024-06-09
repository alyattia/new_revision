// @desc   GET all posts
// @route  GET /posts
// @access  (we don't have authentication here)
const getPosts = (req, res, next) => {
  const id = parseInt(req.params.id); 
  const post = posts.find(post => post.id === id);
  if (!post) {
    const error = new Error(`i am here The post with id ${id} was not found`);
    return next(error);
  }
  
  res.status(200).json(post);
}

module.exports = getPosts