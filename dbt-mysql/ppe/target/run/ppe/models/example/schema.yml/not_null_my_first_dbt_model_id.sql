select
      count(*) as failures,
      case
        when count(*) <> 0 then 'true'
        else 'false'
      end as should_warn,
      case
        when count(*) <> 0 then 'true'
        else 'false'
      end as should_error
    from (
      
    
    



select id
from `hospital_B_ppe_data`.`my_first_dbt_model`
where id is null



      
    ) dbt_internal_test