CREATE TABLE public.collab_changelog (
    event_id INT GENERATED ALWAYS AS IDENTITY,
    event_type TEXT NOT NULL,
    PRIMARY KEY (event_id)
);

