-- RemoteAgentFramework Database Initialization
-- Educational Cybersecurity Simulation Framework
-- VM ISOLATION REQUIRED - FOR EDUCATIONAL USE ONLY

-- Create database (if not exists)
-- Note: Database creation is handled by Docker environment variables

-- Educational framework identification
COMMENT ON DATABASE cyberproject_db IS 'Educational cybersecurity simulation database - VM isolation required';

-- Create extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create educational safety log table
CREATE TABLE IF NOT EXISTS educational_safety_log (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    event_description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_ip INET,
    user_agent TEXT,
    safety_verified BOOLEAN DEFAULT FALSE
);

-- Insert initial safety verification record
INSERT INTO educational_safety_log (event_type, event_description, safety_verified) 
VALUES ('FRAMEWORK_INIT', 'RemoteAgentFramework initialized with educational safety measures', TRUE);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_safety_log_created_at ON educational_safety_log(created_at);
CREATE INDEX IF NOT EXISTS idx_safety_log_event_type ON educational_safety_log(event_type);

-- Educational compliance constraints
ALTER TABLE educational_safety_log 
ADD CONSTRAINT chk_educational_use 
CHECK (event_description LIKE '%educational%' OR event_description LIKE '%Educational%');

-- Grant permissions to application user
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO cyberproject_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO cyberproject_user;

-- Log successful initialization
INSERT INTO educational_safety_log (event_type, event_description, safety_verified) 
VALUES ('DATABASE_INIT', 'Database initialized with educational safety constraints', TRUE);