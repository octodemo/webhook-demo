/*
 * Create a table for a collab changelog proof of concept
 */

CREATE TABLE public.collab_changelog (
    event_id INT GENERATED ALWAYS AS IDENTITY,
    event_type TEXT NOT NULL,
    username VARCHAR NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    target_repo VARCHAR NOT NULL,
    PRIMARY KEY (event_id)
);
