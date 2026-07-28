# Decisions required

The following product/business questions are still unresolved by the current codebase and should be confirmed before further schema evolution:

1. User authentication semantics
   - Current state: the schema has `users.email` and no password hash field in the current models.
   - Options: keep auth out of this service for now; add a `password_hash` field later; or use an external identity provider.
   - Recommended: keep the current schema unchanged for now and let authentication be handled outside this database layer until a clear auth flow exists.
   - Schema impact: adding `password_hash` would require a new migration; using an external provider would not require DB changes here.

2. Enum-like fields stored as integers
   - Current state: `User.role`, `Interview.language`, `Interview.difficulty_level`, `Interview.status`, `SessionStep.type`, `SessionStep.importance_level`, and `SessionStep.difficulty_level` are stored as integers.
   - Options: keep integers for now; introduce SQLAlchemy enums; or switch to strings.
   - Recommended: keep integers for now because no existing API or service layer defines a canonical enum contract.
   - Schema impact: converting to enums or strings would require a dedicated migration and data mapping.

3. Interview-to-session cardinality
   - Current state: `interview_sessions` references `interviews` through a standard foreign key, and the schema does not enforce a single session per interview.
   - Options: one interview can have many sessions; one interview can have at most one active session; or one interview can have exactly one session.
   - Recommended: keep the current one-to-many shape unless the product requirements explicitly require a stricter rule.
   - Schema impact: enforcing a one-to-one or single-active-session rule would need a new constraint or partial unique index.

4. Answer and feedback cardinality
   - Current state: a `session_step` can have multiple `user_answers`, and a `user_answer` can have multiple `answer_feedbacks`.
   - Options: one answer per step; one feedback per answer; or multiple feedback rounds per answer.
   - Recommended: preserve the current one-to-many shape unless the product workflow clearly requires otherwise.
   - Schema impact: tightening this relationship would require new constraints or a schema revision.
