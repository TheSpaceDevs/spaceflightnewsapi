import React from 'react';
import ReactPaginate from "react-paginate";

const PaginateComponent = ({totalPages, setPage}) => {
  return (
    <ReactPaginate
      containerClassName="pagination justify-content-center mb-3 mt-3"
      disabledClassName="disabled"
      pageClassName="page-item"
      pageLinkClassName="page-link"
      previousClassName="page-item"
      nextClassName="page-item"
      nextLinkClassName="page-link"
      previousLinkClassName="page-link"
      activeClassName="active"
      activeLinkClassName="active"
      breakClassName="break-me"
      breakLinkClassName="page-link"
      pageCount={totalPages}
      pageRangeDisplayed={4}
      onPageChange={({selected}) => {
        setPage(selected + 1)
      }}
    >
    </ReactPaginate>
  );
};

export default PaginateComponent;
