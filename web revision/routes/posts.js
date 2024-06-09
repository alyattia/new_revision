const express = require('express');
const router = express.Router();
const getPosts = require('../controllers/postsController')


// dumy data
let posts = [
  {id: 1, title: 'post 1'},
  {id: 2, title: 'post 2'},
  {id: 3, title: 'post 3'},
  {id: 4, title: "post 4"}
]


// getting data
router.get("/:id", getPosts)

// /posts/?limit=2
router.get("/", (req, res, next) => {
  const limit = parseInt(req.query.limit);
  if (!isNaN(limit) && limit > 0) {
    res.status(200).json(posts.slice(0, limit));
  } else {
    res.json(posts)
  }
})

// create a new post
router.post("/", (req, res, next) => {
  const newPost = {
    id: posts.length + 1,
    title: req.body.title
  };
  if (!newPost.title) {
    return res.status(400).json({msg: "please include a title"})
  }
  posts.push(newPost);

  res.status(201).json(posts)
})

// update
router.put("/:id", (req, res, next) => {
  const post = posts.find(post => post.id === parseInt(req.params.id));
  if (!post) {
    return res.status(404).json({msg: `coudn't find a post with id ${req.params.id}`});
  }
  post.title = req.body.title;
  res.status(200).json(posts);
})

// delete
router.delete("/:id", (req, res, next) => {
  const id = parseInt(req.params.id);
  posts = posts.filter(post => post.id !== id);
  res.status(200).json(posts);
})

module.exports = router;
