/* 
 * Create indexes
 */
CREATE INDEX IF NOT EXISTS idx_test_webhook ON public.test_webhook (target_repo);
CREATE INDEX IF NOT EXISTS idx_collabs ON public.collab_changelog (username);