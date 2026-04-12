// Supabase Configuration
// Project: E-Green Solution
const SUPABASE_URL = "https://azduynhaiqvghghsfumv.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF6ZHV5bmhhaXF2Z2hnaHNmdW12Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU5OTcyODcsImV4cCI6MjA5MTU3MzI4N30.fd4uSZBsXOhLBNTSWr0aJcrPOm_9fzJtY23hGkQogW0";

// Initialize Supabase Client
const _supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// EmailJS Configuration
const EMAILJS_PUBLIC_KEY = "b1RLWRUjL7PIz4wOM";
const EMAILJS_SERVICE_ID = "service_0971a17";
const EMAILJS_TEMPLATE_ID = "template_vzc1g5g";
