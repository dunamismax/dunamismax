import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in the .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Pydantic model for a blog post
class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/blog-posts", response_model=List[BlogPost])
async def get_blog_posts():
    try:
        response = supabase.table("blog_posts").select("id,title,content,created_at").execute()
        # Supabase client returns data in response.data
        if response.data:
            return response.data
        return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/blog-posts/{post_id}", response_model=BlogPost)
async def get_blog_post(post_id: int):
    try:
        response = supabase.table("blog_posts").select("id,title,content,created_at").eq("id", post_id).single().execute()
        if response.data:
            return response.data
        raise HTTPException(status_code=404, detail="Blog post not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))