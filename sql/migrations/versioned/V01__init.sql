/*
 * Create a table to store basic webhook payload info for demo
 */

CREATE TABLE public.test_webhook (
    event_id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    target_repo VARCHAR NOT NULL,
    PRIMARY KEY (event_id)
);
