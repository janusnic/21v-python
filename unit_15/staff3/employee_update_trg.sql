create trigger employee_update_trg after update on employee
begin
  update employee set updatedon = datetime('NOW') where emp_id = new.emp_id;
end;