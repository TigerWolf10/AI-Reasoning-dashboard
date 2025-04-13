from supabase import create_client, Client

SUPABASE_URL = "https://eqthofaxyxwsmtvfgewy.supabase.co"   # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVxdGhvZmF4eXh3c210dmZnZXd5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ1MzgxMDUsImV4cCI6MjA2MDExNDEwNX0.SzpPNGb-DqIgi-5GEMFzy8t5CwiBHqFjTq1MCMauCPc"                         # Replace with your Supabase anon/public key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
